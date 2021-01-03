from .utils import send_action

ADMIN_CHAT_ID = 294318373


@send_action(ChatAction.TYPING)
def start_command(bot, update):
    text = 'Dorova'
    bot.send_message(chat_id=update.message.chat_id, text=text)


@send_action(ChatAction.TYPING)
def text_message(bot, update):
    print(update.message)

    bot.send_message(chat_id=update.message.chat_id, text=choice)

    if update.message.chat_id != ADMIN_CHAT_ID:
        message_to_admin = update.message.text + '\n' + 'Bot replied: ' + choice

        bot.send_message(chat_id=ADMIN_CHAT_ID, text=)
        bot.send_message(chat_id=ADMIN_CHAT_ID, text=message_to_admin)
