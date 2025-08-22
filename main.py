import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys
import os
import subprocess
import discord
from discord.ext import commands
import sqlite3
from colorama import Fore, Style, init
import requests
import asyncio
import pkg_resources

def check_and_install_requirements():
    required_packages = {
        'discord.py': 'discord.py',
        'colorama': 'colorama',
        'requests': 'requests',
        'aiohttp': 'aiohttp',
        'python-dotenv': 'python-dotenv',
        'aiohttp-socks': 'aiohttp-socks',
        'pytz': 'pytz',
        'pyzipper': 'pyzipper'
    }
    
    def install_package(package_name):
        try:
            print(f"Installing {package_name}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            print(f"{package_name} installed successfully.")
            return True
        except subprocess.CalledProcessError:
            print(f"Error installing {package_name}.")
            return False

    packages_to_install = []
    try:
        import pkg_resources
        installed_packages = {pkg.key for pkg in pkg_resources.working_set}
    except ImportError:
        install_package('setuptools')
        import pkg_resources
        installed_packages = {pkg.key for pkg in pkg_resources.working_set}

    for package, pip_name in required_packages.items():
        if package.lower() not in installed_packages:
            packages_to_install.append(pip_name)

    if packages_to_install:
        print("Missing libraries detected. Starting installation...")
        for package in packages_to_install:
            success = install_package(package)
            if not success:
                print(f"Some libraries could not be installed. Please run pip install {package} manually.")
                sys.exit(1)
        print("All required libraries installed!")
        return True
    return False

VERSION_URL = "https://raw.githubusercontent.com/Reloisback/Whiteout-Survival-Discord-Bot/refs/heads/main/autoupdateinfo.txt"

def restart_bot():
    print(Fore.YELLOW + "\nRestarting bot..." + Style.RESET_ALL)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def setup_version_table():
    try:
        with sqlite3.connect('db/settings.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS versions (
                file_name TEXT PRIMARY KEY,
                version TEXT,
                is_main INTEGER DEFAULT 0
            )''')
            conn.commit()
            print(Fore.GREEN + "Version table created successfully." + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error creating version table: {e}" + Style.RESET_ALL)

async def check_and_update_files():
    try:
        try:
            response = requests.get(VERSION_URL)
            if response.status_code == 200:
                source_url = "https://raw.githubusercontent.com/Reloisback/Whiteout-Survival-Discord-Bot/refs/heads/main"
                print(Fore.GREEN + "Connected to GitHub successfully." + Style.RESET_ALL)
            else:
                raise requests.RequestException
        except requests.RequestException:
            print(Fore.YELLOW + "Cannot connect to GitHub, trying alternative source (wosland.com)..." + Style.RESET_ALL)
            alt_version_url = "https://wosland.com/wosdc/autoupdateinfo.txt"
            response = requests.get(alt_version_url)
            if response.status_code == 200:
                source_url = "https://wosland.com/wosdc"
            else:
                print(Fore.RED + "Cannot connect to any source." + Style.RESET_ALL)
                return False

        if not os.path.exists('cogs'):
            os.makedirs('cogs')
            print(Fore.GREEN + "cogs folder created" + Style.RESET_ALL)

        content = response.text.split('\n')
        documents = {}
        main_py_updated = False

        doc_section = False
        for line in content:
            if line.startswith("Documants;"):
                doc_section = True
                continue
            elif doc_section and line.startswith("Updated Info;"):
                break
            elif doc_section and '=' in line:
                file_name, version = [x.strip() for x in line.split('=')]
                documents[file_name] = version

        update_notes = []
        update_section = False
        for line in content:
            if line.startswith("Updated Info;"):
                update_section = True
                continue
            if update_section and line.strip():
                update_notes.append(line.strip())

        updates_needed = []
        with sqlite3.connect('db/settings.sqlite') as conn:
            cursor = conn.cursor()
            
            for file_name, new_version in documents.items():
                cursor.execute("SELECT version FROM versions WHERE file_name = ?", (file_name,))
                result = cursor.fetchone()
                
                if result is None:
                    updates_needed.append((file_name, "File and No Version", new_version))
                elif result[0] != new_version:
                    updates_needed.append((file_name, result[0], new_version))

        if updates_needed:
            print("\nUpdates available!")
            print("\nIf this is your first installation and you see File and No version, please update!")
            print("\nFiles to update:")
            for file_name, old_version, new_version in updates_needed:
                print(f"• {file_name}: {old_version} -> {new_version}")

            if update_notes:
                print("\nUpdate Notes:")
                for note in update_notes:
                    print(f"• {note}")

            if any("main.py" in file_name for file_name, _, _ in updates_needed):
                print("\nNOTE: This update includes changes to main.py. Bot will restart after update.")

            response = input("\nDo you want to update now? (y/n): ").lower().strip()
            if response == 'y':
                print("\nStarting update process...")
                
                for file_name, old_version, new_version in updates_needed:
                    try:
                        if file_name == "main.py":
                            file_url = f"{source_url}/main.py"
                        else:
                            file_url = f"{source_url}/cogs/{file_name}"
                        
                        file_response = requests.get(file_url)
                        if file_response.status_code == 200:
                            with open(file_name, 'w', encoding='utf-8') as f:
                                f.write(file_response.text)
                            
                            cursor.execute("INSERT OR REPLACE INTO versions (file_name, version) VALUES (?, ?)", (file_name, new_version))
                            print(f"✓ {file_name} updated to {new_version}")
                        else:
                            print(f"✗ Failed to download {file_name}")
                    except Exception as e:
                        print(f"✗ Error updating {file_name}: {e}")

                conn.commit()
                print("\nAll updates completed successfully!")
                
                if any("main.py" in file_name for file_name, _, _ in updates_needed):
                    print("\nRestarting bot to apply main.py updates...")
                    restart_bot()
                
                return True
            else:
                print("Update cancelled.")
                return False
        else:
            print("No updates available.")
            return False

    except Exception as e:
        print(Fore.RED + f"Error during version check: {e}" + Style.RESET_ALL)
        return False

class CustomBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.guild_id = kwargs.pop('guild_id', None)
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"{Fore.GREEN}Bot connecté en tant que {Fore.CYAN}{self.user}{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Bot est dans {len(self.guilds)} serveur(s){Style.RESET_ALL}")
        
        for guild in self.guilds:
            print(f"{Fore.CYAN}Serveur: {guild.name} (ID: {guild.id}){Style.RESET_ALL}")
        
        # Synchroniser les commandes slash avec le serveur spécifique
        if self.guild_id:
            try:
                guild = discord.Object(id=int(self.guild_id))
                self.tree.copy_global_to(guild=guild)
                synced = await self.tree.sync(guild=guild)
                print(f"{Fore.GREEN}Commandes slash synchronisées avec le serveur {self.guild_id}: {len(synced)}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Erreur lors de la synchronisation des commandes: {e}{Style.RESET_ALL}")
        else:
            try:
                synced = await self.tree.sync()
                print(f"{Fore.GREEN}Commandes slash synchronisées globalement: {len(synced)}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Erreur lors de la synchronisation des commandes: {e}{Style.RESET_ALL}")

    async def on_error(self, event_name, *args, **kwargs):
        if event_name == "on_interaction":
            error = sys.exc_info()[1]
            if isinstance(error, discord.NotFound) and error.code == 10062:
                return
        
        await super().on_error(event_name, *args, **kwargs)

    async def on_command_error(self, ctx, error):
        if isinstance(error, discord.NotFound) and error.code == 10062:
            return
        await super().on_command_error(ctx, error)

async def load_cogs():
    cog_files = [
        "cogs.alliance",
        "cogs.alliance_member_operations", 
        "cogs.bot_operations",
        "cogs.changes",
        "cogs.control",
        "cogs.gift_operations",
        "cogs.logsystem",
        "cogs.olddb",
        "cogs.other_features",
        "cogs.support_operations",
        "cogs.w",
        "cogs.wel"
    ]
    
    for cog in cog_files:
        try:
            await bot.load_extension(cog)
            print(f"✓ Loaded {cog}")
        except Exception as e:
            print(f"✗ Failed to load {cog}: {e}")

async def main():
    global bot
    
    if not os.path.exists('db'):
        os.makedirs('db')
        print(Fore.GREEN + "db folder created" + Style.RESET_ALL)

    setup_version_table()
    
    await check_and_update_files()
    
    # Chargement des variables d'environnement depuis .env
    from dotenv import load_dotenv
    load_dotenv()
    
    bot_token = os.getenv('BOT_TOKEN')
    guild_id = os.getenv('GUILD_ID')
    channel_id = os.getenv('CHANNEL_ID')
    alliance_name = os.getenv('ALLIANCE_NAME')
    secret = os.getenv('SECRET')
    
    intents = discord.Intents.default()
    intents.message_content = True

    bot = CustomBot(command_prefix='/', intents=intents, guild_id=guild_id)

    init(autoreset=True)
    
    if not bot_token:
        print(Fore.RED + "BOT_TOKEN manquant dans settings.txt!" + Style.RESET_ALL)
        sys.exit(1)
    
    if not guild_id:
        print(Fore.RED + "GUILD_ID manquant dans settings.txt!" + Style.RESET_ALL)
        sys.exit(1)
    
    print(Fore.GREEN + f"Configuration chargée: Guild ID: {guild_id}, Channel ID: {channel_id}, Alliance: {alliance_name}" + Style.RESET_ALL)

    databases = {
        "conn_alliance": "db/alliance.sqlite",
        "conn_giftcode": "db/giftcode.sqlite",
        "conn_changes": "db/changes.sqlite",
        "conn_users": "db/users.sqlite",
        "conn_settings": "db/settings.sqlite",
    }

    connections = {name: sqlite3.connect(path) for name, path in databases.items()}

    print(Fore.GREEN + "Database connections have been successfully established." + Style.RESET_ALL)

    def create_tables():
        with connections["conn_changes"] as conn_changes:
            conn_changes.execute('''CREATE TABLE IF NOT EXISTS nickname_changes (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                fid INTEGER, 
                old_nickname TEXT, 
                new_nickname TEXT, 
                change_date TEXT
            )''')
            conn_changes.execute('''CREATE TABLE IF NOT EXISTS furnace_changes (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                fid INTEGER, 
                old_furnace_lv INTEGER, 
                new_furnace_lv INTEGER, 
                change_date TEXT
            )''')

        with connections["conn_settings"] as conn_settings:
            conn_settings.execute('''CREATE TABLE IF NOT EXISTS botsettings (
                id INTEGER PRIMARY KEY, 
                channelid INTEGER, 
                giftcodestatus TEXT 
            )''')
            conn_settings.execute('''CREATE TABLE IF NOT EXISTS admin (
                id INTEGER PRIMARY KEY, 
                is_initial INTEGER
            )''')

        with connections["conn_users"] as conn_users:
            conn_users.execute('''CREATE TABLE IF NOT EXISTS users (
                fid INTEGER PRIMARY KEY, 
                nickname TEXT, 
                furnace_lv INTEGER DEFAULT 0, 
                kid INTEGER, 
                stove_lv_content TEXT, 
                alliance TEXT
            )''')

        with connections["conn_giftcode"] as conn_giftcode:
            conn_giftcode.execute('''CREATE TABLE IF NOT EXISTS gift_codes (
                giftcode TEXT PRIMARY KEY, 
                date TEXT
            )''')
            conn_giftcode.execute('''CREATE TABLE IF NOT EXISTS user_giftcodes (
                fid INTEGER, 
                giftcode TEXT, 
                status TEXT, 
                PRIMARY KEY (fid, giftcode),
                FOREIGN KEY (giftcode) REFERENCES gift_codes (giftcode)
            )''')

        with connections["conn_alliance"] as conn_alliance:
            conn_alliance.execute('''CREATE TABLE IF NOT EXISTS alliance_members (
                fid INTEGER PRIMARY KEY, 
                nickname TEXT, 
                furnace_lv INTEGER DEFAULT 0, 
                kid INTEGER, 
                stove_lv_content TEXT, 
                alliance TEXT
            )''')

        print(Fore.GREEN + "All tables checked." + Style.RESET_ALL)

    create_tables()
    
    await load_cogs()
    
    try:
        await bot.start(bot_token)
    except discord.LoginFailure:
        print(Fore.RED + "Invalid bot token. Please check your bot token and try again." + Style.RESET_ALL)
        os.remove(token_file)
        sys.exit(1)
    except Exception as e:
        print(Fore.RED + f"Error starting bot: {e}" + Style.RESET_ALL)
        sys.exit(1)

if __name__ == "__main__":
    check_and_install_requirements()
    asyncio.run(main())