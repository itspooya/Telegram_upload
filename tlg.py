
import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from downloader import download
import os
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi This A bot To Upload Files to Telegram')



def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text("Downloading {}".format(update.message.text))
    f = download(update.message.text)
    Bt = telegram.Bot(token="926175130:AAG-j9CWDZREiQzGFYxNS2Q-OJiKkp7-jcc")
    with open(f,'rb') as file:
        Bt.send_document(update.message.chat_id,file,timeout=1000)
    os.remove(f)



def error(bot, update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()