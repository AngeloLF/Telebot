from telegram import Bot, InputFile
import coloralf as c
import os, sys, asyncio
path_home = os.path.expanduser("~/")
import params




async def asyncSending(texts, bot_token, userIDs, printage=True):
    """
    Fonction asynchrone qui permet d'envoyer le message

    Params:
        texts [lsit(str)]   : liste d'str a envoyer par le bot
        bot_token [str]     : token du bot
        userIDs [lsit(str)] : liste des IDs des users
        printage [bool]     : Si True, affiche les print pour chaque envoie
    """


    try:

        bot = Bot(bot_token)
        bot_name_class = await bot.getMyName()
        bot_name = bot_name_class.name


        # On itère sur les texts
        for t in texts:

            # On itère sur les users
            for user in userIDs:

                await bot.send_message(chat_id=user, text=f"{t}")
                if printage : print(f"{c.ti}<{c.y}{bot_name}{c.d}{c.ti}> send to ID={c.ly}{user}{c.d}{c.ti} : {c.y}{t}{c.d}")

    except Exception as e:

        print(f"{c.r}WARNING [in telebot.py] : {e}{c.d}")




def send_message(texts, folder_ids=None, folder_bot=None, printage=True):
    """
    Fonction send_message. Permet d'envoyer le(s) str donné dans `texts`

    Params:
        texts [str, list[str]] : Str ou list d'str a envoyer par le bot
        folder_ids [str]       : Dossier avec des `.txt` qui contienne les users IDs. Si `None`, le FOLDER_IDS donné par `params.py` est choisi (prefered).
        folder_bot [str]       : Dossier avec `bot_token.txt` qui contient le token du bot. Si `None`, le FOLDER_BOT donné par `params.py` est choisi (prefered).
    """


    # Define folders with users IDs and bot token
    folder_ids = params.FOLDER_IDS if folder_ids is None else folder_ids
    folder_bot = params.FOLDER_BOT if folder_bot is None else folder_bot


    # Recup. user IDs
    userIDs = list()
    for file in os.listdir(folder_ids):
        with open(f"{folder_ids}/{file}", "r") as f: 
            userIDs.append(f.read())


    # Recup. bot token
    with open(f"{folder_bot}/bot_token.txt", "r") as f:
        bot_token = f.read() 


    # Si texts est un str, on le met dans une liste
    texts = text if isinstance(text, (list)) else [text]


    # run asyncSending 
    asyncio.run(asyncSending(texts, bot_token, userIDs, printage))





if __name__ == '__main__':
    

    if "test" in sys.argv[1:]:

        print(f"Begin test ...")

        send_message("Test solo")
        send_message(["Test combiner...", 12.3, "... c'est bon"])

        print(f"Test end.")
    
    else:

        text = None
        folder_ids = None
        folder_bot = None

        for argv in sys.argv[1:]:

            if argv[:5] == "text=" : text = argv[5:]
            if argv[:5] == "fids=" : folder_ids = argv[5:]
            if argv[:5] == "fbot=" : folder_bot = argv[5:]


        send_message(text, folder_ids=folder_ids, folder_bot=folder_bot)
