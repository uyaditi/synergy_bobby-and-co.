from telegram.ext.updater import Updater
updater = Updater("6373910131:AAEIoEv4w2rC7AzVtHeniPX1BOLrsOTlJlA", use_context=True)

def send_msg(text, chat_id):
    updater.bot.sendMessage(chat_id, text)