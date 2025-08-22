# 🚀 Guide d'Installation - Bot Discord Whiteout Survival V4

## 📋 Prérequis

### **1. Système d'exploitation**
- ✅ **Windows 10/11** (recommandé)
- ✅ **Windows 7/8** (peut fonctionner)

### **2. Python**
- ✅ **Python 3.8 ou plus récent** (recommandé: Python 3.11)


---

## 🐍 Installation de Python

### **Étape 1 : Télécharger Python**
1. Va sur [python.org](https://www.python.org/downloads/)
2. Clique sur **"Download Python 3.11.x"** (le gros bouton jaune)
3. **IMPORTANT** : Coche la case **"Add Python to PATH"** ✅

### **Étape 2 : Installer Python**
1. Double-clique sur le fichier téléchargé
2. Clique sur **"Install Now"**
3. Attends que l'installation se termine
4. Clique sur **"Close"**

### **Étape 3 : Vérifier l'installation**
1. Appuie sur **Windows + R**
2. Tape **"cmd"** et appuie sur Entrée
3. Dans la console, tape : `python --version`
4. Tu devrais voir : `Python 3.11.x`

---

## 🤖 Installation du Bot

### **Étape 1 : Télécharger le projet**
1. Télécharge le projet depuis GitHub
2. Extrais le fichier ZIP dans un dossier (ex: `C:\BotDiscord\`)
3. Ouvre ce dossier

### **Étape 2 : Installer les dépendances**
1. Dans le dossier du projet, appuie sur **Shift + Clic droit**
2. Sélectionne **"Ouvrir la fenêtre PowerShell ici"**
3. Dans PowerShell, tape cette commande :
```powershell
py -m pip install -r requirements.txt
```
4. Attends que l'installation se termine (peut prendre 5-10 minutes)

### **Étape 3 : Configurer le bot**
1. Dans le dossier du projet, trouve le fichier `.env`
2. Ouvre-le avec **Bloc-notes** (clic droit → Ouvrir avec → Bloc-notes)
3. Remplis les informations :

```env
# Token de ton bot Discord
BOT_TOKEN=ton_token_ici

# ID de ton serveur Discord
GUILD_ID=ton_guild_id_ici

# ID du canal où le bot enverra les messages
CHANNEL_ID=ton_channel_id_ici

# Nom de ton alliance
ALLIANCE_NAME=NomDeTonAlliance

# Clé secrète (changer le secret "chaque bot ont leurs propre secret")
SECRET=dLbxbErMUO8NUFcQxrxyfco_auZdQwA-
```

---

## 🔑 Obtenir les informations Discord

### **1. BOT_TOKEN**
1. Va sur [Discord Developer Portal](https://discord.com/developers/applications)
2. Clique sur **"New Application"**
3. Donne un nom à ton bot
4. Va dans **"Bot"** dans le menu de gauche
5. Clique sur **"Reset Token"** puis **"Copy"**
6. Colle ce token dans le fichier `.env`

### **2. GUILD_ID (ID du serveur)**
1. Dans Discord, va dans **Paramètres** → **Avancés**
2. Active **"Mode développeur"**
3. Fais clic droit sur ton serveur → **"Copier l'identifiant"**
4. Colle cet ID dans le fichier `.env`

### **3. CHANNEL_ID (ID du canal)**
1. Toujours en mode développeur
2. Fais clic droit sur le canal → **"Copier l'identifiant"**
3. Colle cet ID dans le fichier `.env`

---

## 🚀 Lancer le Bot

### **Étape 1 : Démarrer le bot**
1. Dans PowerShell (dans le dossier du projet)
2. Tape : `py main.py`
3. Le bot devrait se connecter !

### **Étape 2 : Vérifier que ça marche**
1. Dans Discord, tu devrais voir ton bot en ligne (point vert)
2. Essaie de taper `/gift` dans un canal
3. Si ça marche, félicitations ! 🎉

---

## ❌ Problèmes courants

### **"Python n'est pas reconnu"**
- Réinstalle Python en cochant **"Add Python to PATH"**
- Redémarre ton ordinateur

### **"Module not found"**
- Vérifie que tu es dans le bon dossier
- Relance : `py -m pip install -r requirements.txt`

### **"Invalid token"**
- Vérifie que ton token est correct dans le fichier `.env`
- Vérifie que ton bot est invité dans ton serveur

### **"Bot ne répond pas"**
- Vérifie que le bot a la permission **"Utiliser les commandes slash"**
- Vérifie que le GUILD_ID est correct

---

## 🔧 Inviter le Bot dans ton Serveur

### **Étape 1 : Créer le lien d'invitation**
1. Dans [Discord Developer Portal](https://discord.com/developers/applications)
2. Sélectionne ton application
3. Va dans **"OAuth2"** → **"URL Generator"**
4. Coche ces permissions :
   - ✅ `bot`
   - ✅ `applications.commands`
   - ✅ `Send Messages`
   - ✅ `Read Message History`
   - ✅ `Use Slash Commands`
5. Copie l'URL générée

### **Étape 2 : Inviter le bot**
1. Ouvre l'URL copiée dans ton navigateur
2. Sélectionne ton serveur
3. Clique sur **"Autoriser"**

---

## 📞 Besoin d'aide ?

Si tu as des problèmes :
1. **Vérifie que tu as suivi TOUTES les étapes**
2. **Regarde les messages d'erreur dans PowerShell**
3. **Demande de l'aide sur Discord** (Reloisback)

---

## 🎯 Commandes disponibles

Une fois le bot connecté, tu peux utiliser :
- `/gift` - Voir les codes cadeaux
- `/w [ID]` - Info d'un joueur
- `/allist` - Liste de ton alliance
- `/allistadd [ID]` - Ajouter un membre
- `/nickname [ID]` - Historique des noms
- `/furnace [ID]` - Historique des niveaux

---

**🎉 Félicitations ! Tu as installé ton bot Discord !**
