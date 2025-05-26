# Telebot

Bot Telegram qui permet d'envoyer un / des message(s) à une ou plusieurs personnes.

Faire `python Telebot/telebot.py test` pour faire un test, après avoir créé les dossiers avec les ids et le token du bot, comme écrit ci-dessous.
Les dossiers fonder_ids et folder_bot sont en.gitignore.


## Quelques info

Le bot Telegram a besoin de deux choses :


### Les "ID" de destinations des messages. 
Pour les connaître, il faut envoyer un message "@userinfobot" sur Telegram, et lui envoyer "/start".
Il répondra quelque chose comme :
```
Id: **********
First: Prenom
Last: Nom
Lang: fr
```
Il faut créer un dossier, nommé par défaut `folder_ids`, où seront mis des fichiers `.txt` contenant uniquement l'ID.
Par exemple `angelo.txt`, avec à l'intérieur "1000000000". Le nom avant le.txt sera utilisé pour l'envoi de print.
Le chemin et le nom de ce dossier `folder_ids` sont définis dans le `params.py`. Il peut aussi être donné directement dans l'appel de la fonction.

### Le token du bot
Il faut créer un bot. Pour cela, il faut demander un "/newbot" à "@BotFather". Il faut ensuite mettre le token qui sera donné dans un `bot_token.txt`, dans un dossier `folder_bot`.


### Appeler la fonction
Enfin pour envoyer un/des messages, on peut appeler la fonction `send_message` tel que :

```
texts = "Mon message"

folder_ids = "./Telebot/folder_ids"
folder_bot = "./Telebot/folder_bot"

send_message(texts, folder_ids, folder_bot, printable=True)
```

Le printable permet, si voulu, d'envoyer des print a chaque message. Il est par default a True.


## Pip install

* `pip install python-telegram-bot`
* `pip install coloralf`