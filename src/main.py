from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

from .utils import send_action


with open('token.txt', 'r') as f:
    token = f.readline()

updater = Updater(token=token)
dispatcher = updater.dispatcher
j = dispatcher.job_queue

admin_chat_id = 294318373


@send_action(ChatAction.TYPING)
def start_command(bot, update):
    text = 'Dorova'
    bot.send_message(chat_id=update.message.chat_id, text=text)


@send_action(ChatAction.TYPING)
def text_message(bot, update):
    print(update.message)

    bot.send_message(chat_id=update.message.chat_id, text=choice)

    if update.message.chat_id != admin_chat_id:
        message_to_admin = update.message.text + '\n' + 'Bot replied: ' + choice
        
        bot.send_message(chat_id=admin_chat_id, text=)
        bot.send_message(chat_id=admin_chat_id, text=message_to_admin)


def main():
    start_command_handler = CommandHandler('start', start_command)
    text_message_handler = MessageHandler(Filters.text, text_message)
    sticker_message_handler = MessageHandler(Filters.sticker, sticker_message)

    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)
    dispatcher.add_handler(sticker_message_handler)

    updater.start_polling(clean=True)

    updater.idle()


if __name__ == '__main__':
    main()
