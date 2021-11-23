from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests,os
from dotenv import load_dotenv,dotenv_values
import json

#load_dotenv()

#TELEGRAM_BOT_TOKEN=os.getenv('TELEGRAM_BOT_TOKEN')

config = dotenv_values(".env")
TELEGRAM_BOT_TOKEN=config['TELEGRAM_BOT_TOKEN']
ALLOWED_USERS=json.loads(config['ALLOWED_USERS'])
print(ALLOWED_USERS)

def check_if_allowed_user(userid):
    return userid in ALLOWED_USERS

def ip(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    if not check_if_allowed_user(user['id']):
        return
    """Send a message containing public ip when the command /ip is issued."""
    r = requests.get('http://httpbin.org/get')
    update.message.reply_text(r.json()["origin"])


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("ip", ip))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
