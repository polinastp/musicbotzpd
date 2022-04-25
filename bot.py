from importlib.metadata import entry_points
from re import U
from telegram.ext import Updater, CommandHandler
import settings
import logging 

from functions import start, stop, conv_handler
    
logging.basicConfig(filename='bot.log', level=logging.INFO)



def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher


    #Calling handlers
    dp.add_handler(conv_handler)
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("stop", stop))
    
    logging.info("Bot is working!")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()