import telegram
import logging

from telegram.ext import Updater, CommandHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
	update.message.reply_text("Hey guys! What's up?")

def help(bot, update):
	update.message.reply_text("Help?!")

updater = Updater('YOUR_TELEGRAM_TOKEN_HERE')
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.start_polling()
updater.idle()