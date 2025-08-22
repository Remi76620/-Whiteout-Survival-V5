
<a href="https://www.buymeacoffee.com/reloisback" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

Le projet de bot actuel est actuellement gratuit comme vous le savez.
La version actuelle et toutes les versions futures resteront toujours gratuites.
Les mises à jour peuvent être retardées, mais en même temps je travaille dur et j'essaie de m'occuper de ma famille, et je continue à développer le projet chaque fois que je peux.
V2 peut sembler ancienne mais nous partageons encore des mises à jour sur Discord, maintenant V3.2 est partagée sur Discord et je continue à développer V4 en même temps.

Mon bouton café est toujours actif si vous voulez aider.
Je vous aime pour utiliser mon bot et merci beaucoup pour vos gentils messages

# Bot Discord Whiteout Survival V5

**Après plusieurs améliorations et optimisations, je présente la version V4 plus stable, sécurisée et riche en fonctionnalités du bot.**

[![Comment Installer ?](https://github.com/Reloisback/test/blob/main/howinstall.png?raw=true)](https://youtu.be/sWPjBpMhb3s)

### 🆕 Quoi de Neuf dans V4 ?

### **🔐 Sécurité renforcée**
* **Configuration sécurisée** : Migration vers le système `.env` pour protéger vos informations sensibles
* **Gestion des permissions** : Vérification automatique des permissions Discord
* **Protection des données** : Fichiers sensibles automatiquement ignorés par Git

### **⚡ Performance améliorée**
* **Gestion des erreurs** : Meilleure gestion des erreurs API et des timeouts
* **Synchronisation intelligente** : Commandes slash synchronisées automatiquement avec votre serveur
* **Base de données optimisée** : Structure de base de données améliorée et plus rapide

### **🎁 Commandes améliorées**
* **`/gift`** : Vérification automatique des codes cadeaux avec retry intelligent (20 tentatives)
* **`/w`** : Affichage correct des niveaux FC avec images correspondantes
* **`/allist`** : Interface plus compacte et mobile-friendly
* **`/nickname` & `/furnace`** : Historique complet des changements avec dates

### **/w**
* Cette commande, qui vous permet de voir les détails et images des membres spécifiés, a été mise à jour.
* Elle affiche maintenant correctement le niveau FC, et l'image de niveau correspondante apparaît dans le message embed.
* Quand vous utilisez `/w`, vous pouvez rechercher des utilisateurs par nom ou ID et voir s'ils sont enregistrés dans la base de données.
* Si la limite d'API est atteinte, au lieu d'une erreur, le bot attend puis affiche le résultat.

### **/addadmin**
* L'autorisation d'administrateur a été ajoutée pour limiter les commandes lourdes en API. Seuls les administrateurs peuvent utiliser les commandes gift, add et remove user.

### **/nickname - /furnace**
* Chaque changement est maintenant sauvegardé dans la base de données. Il vous notifiait auparavant des changements de nom et des mises à jour de niveau de four, mais enregistre maintenant aussi ces changements.
* Lors de l'utilisation de `/nickname` ou `/furnace`, vous pouvez entrer un ID ou sélectionner un utilisateur dans la base de données. Vous verrez l'historique des changements de nom, les dates et les noms précédents.

### **/allist**
* Auparavant, voir une liste d'alliance de 100 personnes la divisait en 4-5 embeds, créant un encombrement visuel. Maintenant c'est plus compact et minimal.

### Visuels des Nouvelles Commandes

#### **`/allistadd`**
* Cette commande vous permet d'ajouter des personnes à la liste d'alliance, soit une par une soit par lots.
* Utilisez `/allistadd ID` pour une personne ou `/allistadd ID1,ID2,ID3` pour plusieurs entrées.

![Allistadd](https://github.com/Reloisback/test/blob/main/allistadd.png?raw=true)

#### **`/allist`**
* Cette commande affiche votre liste d'alliance actuelle.

![Allist](https://github.com/Reloisback/test/blob/main/allist.png?raw=true)

#### **`/gift`**
* Échangez le code cadeau pour les membres de l'alliance, livrant les cadeaux directement dans leur boîte de réception.

![Gift 1](https://github.com/Reloisback/test/blob/main/gift1.png?raw=true)
![Gift 2](https://github.com/Reloisback/test/blob/main/gift2.png?raw=true)
![Gift 3](https://github.com/Reloisback/test/blob/main/gift3.png?raw=true)

#### **`/nickname - /furnace`**
* Montre le nombre de fois qu'une personne a changé son nom et les dates.

![Nickname Furnace](https://github.com/Reloisback/test/blob/main/nicknamefurnace.png?raw=true)

## Description

Ce bot est développé pour les joueurs de Whiteout Survival pour améliorer leur expérience de canal Discord.
Le bot vous notifie quand les membres de l'Alliance changent leur niveau de four ou leur nom en jeu.

---
![Changements de Niveau de Four](https://serioyun.com/gif/1.png)
![Informations Utilisateur](https://serioyun.com/gif/2.png)
![Changements de Surnom](https://serioyun.com/gif/3.png)
![LISTE D'ALLIANCE](https://serioyun.com/gif/4.png)

## 🚀 Comment Utiliser ?

### **📋 Installation rapide**
1. **Téléchargez** le projet depuis GitHub
2. **Installez Python** (version 3.8+ recommandée)
3. **Installez les dépendances** : `py -m pip install -r requirements.txt`
4. **Configurez le fichier `.env`** (voir ci-dessous)
5. **Lancez le bot** : `py main.py`

### **⚙️ Configuration**
Avant de commencer, configurez le fichier `.env` avec :
- `BOT_TOKEN` - Token de votre bot Discord
- `GUILD_ID` - ID de votre serveur Discord
- `CHANNEL_ID` - ID du canal de notifications
- `ALLIANCE_NAME` - Nom de votre alliance
- `SECRET` - Clé secrète (ne changez pas)

**📖 Guide complet** : Consultez `GUIDE-INSTALLATION.md` pour des instructions détaillées !

### **🆕 Nouvelles fonctionnalités V5**

#### **🔐 Sécurité renforcée**
- **Fichier `.env`** : Configuration sécurisée et protégée
- **Permissions automatiques** : Vérification des droits Discord
- **Protection Git** : Fichiers sensibles automatiquement ignorés

#### **⚡ Performance optimisée**
- **Gestion d'erreurs intelligente** : Retry automatique des requêtes API
- **Synchronisation des commandes** : Commandes slash mises à jour automatiquement
- **Base de données optimisée** : Requêtes plus rapides et efficaces

#### **🔄 Mise à jour automatique**
- **Vérification GitHub** : Détection automatique des nouvelles versions
- **Mise à jour intelligente** : Téléchargement et installation automatiques
- **Redémarrage automatique** : Application des mises à jour sans intervention

### **🎮 Commandes Discord**

#### Ajouter et Supprimer des Membres

- Pour ajouter un membre :
```
/allistadd playerID
```

- Pour ajouter plusieurs joueurs :
```
/allistadd playerID1,playerID2,playerID3
```
Limite recommandée : 10 ajouts à la fois pour éviter les bannissements temporaires d'API.

- Pour supprimer un membre :
```
/allistremove playerID
```

- Pour voir la liste d'alliance :
```
/allist
```

- Pour mettre à jour manuellement la liste :
```
/updateallist
```

- Pour des informations détaillées sur le joueur et photos de profil :
```
/w playerID
```

*Note* : Évitez les actualisations manuelles pendant les mises à jour de la liste d'alliance.

Pour changer l'intervalle de mise à jour automatique, modifiez la ligne `@tasks.loop(minutes=20)` à votre intervalle souhaité.

---

## Informations de Support

Ce bot est fourni gratuitement par Reloisback pour les utilisateurs de Whiteout Survival sur Discord.
Si vous avez besoin d'aide, ajoutez Reloisback sur Discord. Pour une aide de configuration 24/7 sur un serveur Windows, contactez-moi pour un support gratuit.

Pour soutenir les projets futurs, considérez un don :
- USDT Tron (TRC20): TC3y2crhRXzoQYhe3rMDNzz6DSrvtonwa3
- USDT Ethereum (ERC20): 0x60acb1580072f20f008922346a83a7ed8bb7fbc9

Merci !

---

## 📁 Fichiers du projet

### **🔧 Fichiers de configuration**
- **`.env`** - Configuration sécurisée du bot (à personnaliser)
- **`requirements.txt`** - Dépendances Python nécessaires
- **`.gitignore`** - Protection des fichiers sensibles

### **📖 Documentation**
- **`README.md`** - Ce fichier (présentation générale)
- **`GUIDE-INSTALLATION.md`** - Guide d'installation détaillé

### **🤖 Code source**
- **`main.py`** - Fichier principal du bot
- **`cogs/`** - Modules de fonctionnalités
- **`db/`** - Bases de données (créées automatiquement)

---

## 🚀 Démarrage rapide

```bash
# 1. Installer les dépendances
py -m pip install -r requirements.txt

# 2. Configurer le fichier .env
# 3. Lancer le bot
py main.py
```

---

## 📞 Support et assistance

- **Discord** : Ajoutez Reloisback pour de l'aide
- **Documentation** : Consultez `GUIDE-INSTALLATION.md`
- **Problèmes** : Vérifiez la section "Problèmes courants" du guide

**🌟 Merci d'utiliser le Bot Discord Whiteout Survival V4 !**

---

## Informations du Développeur

Bonjour, ce bot a été créé gratuitement par Reloisback le 18.10.2024 pour que les utilisateurs de Whiteout Survival puissent l'utiliser dans leurs canaux Discord.
Si vous ne savez pas utiliser Python, vous pouvez me contacter en ajoutant Reloisback comme ami sur Discord ; je serai ravi de vous aider.
Si vous achetez un serveur Windows et que vous ne savez toujours pas comment l'installer et que vous voulez que le bot fonctionne 24/7, vous pouvez encore me contacter. Je peux vous fournir un support gratuit et vous aider avec l'installation.
Comme je l'ai dit encore une fois, ces codes sont entièrement gratuits et je ne demande aucun paiement à qui que ce soit.

Mais si un jour vous voulez me soutenir, voici mes informations de crypto-monnaie :
- USDT Tron (TRC20): TC3y2crhRXzoQYhe3rMDNzz6DSrvtonwa3
- USDT Ethereum (ERC20): 0x60acb1580072f20f008922346a83a7ed8bb7fbc9

Je n'oublierai jamais vos soutiens et je continuerai à développer ce genre de projets gratuitement.

Merci !
