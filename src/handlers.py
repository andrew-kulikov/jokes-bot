from telegram import ChatAction

from utils import send_action
from generator import generate_joke


@send_action(ChatAction.TYPING)
def start_command(update, context):
    text = 'Dorova'
    context.bot.send_message(chat_id=update.message.chat_id, text=text)


@send_action(ChatAction.TYPING)
def text_message(update, context):
    print(update.message)

    joke = generate_joke()
    context.bot.send_message(chat_id=update.message.chat_id, text=joke)
