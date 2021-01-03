from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ChatAction

from .handlers import start_command, text_message


with open('token.txt', 'r') as f:
    token = f.readline()

updater = Updater(token=token)
dispatcher = updater.dispatcher


def main():
    start_command_handler = CommandHandler('start', start_command)
    text_message_handler = MessageHandler(Filters.text, text_message)
    sticker_message_handler = MessageHandler(Filters.sticker, sticker_message)

    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)

    updater.start_polling(clean=True)

    updater.idle()


if __name__ == '__main__':
    main()
