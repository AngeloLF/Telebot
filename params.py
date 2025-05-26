

def __getattr__(name):

    if name in locals() : return locals()[name]
    else : raise ValueError(f"params (of Telebot.params) dont have {name=}.")



FOLDER_IDS = "./Telebot/folder_ids"
FOLDER_BOT = "./Telebot/folder_bot"