# -*- coding: utf-8 -*-

from functions import *

bot = telegram.Bot(TOKEN)

#Function: main
#Main function that run the bot.
def main():
	updater = Updater(TOKEN)
	dp = updater.dispatcher

	#Bot Command
    

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()
