import logging
import os
import random
import requests
import re
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# def get_url():
# 	contents = requests.get('https://random.dog/woof.json').json()
# 	url = contents['url']
# 	return url

# def get_image_url():
# 	allowed_extension = ['jpg','jpeg','png']
# 	file_extension = ''
# 	while file_extension not in allowed_extension:
# 			url = get_url()
# 			file_extension = re.search("([^.]*)$",url).group(1).lower()
# 	return url

# def bop(bot, update):
# 	url = get_image_url()
# 	chat_id = update.message.chat_id
# 	bot.send_photo(chat_id=chat_id, photo=url)

def start(bot, update):
	"""Send a message when the command /start is issued."""
	update.message.reply_text('Hola soy Manzano Bot!')
	#bot.send_message(chat_id=update.message.chat_id, text="Hola soy Manzano Bot!")

def help(bot, update):
	"""Send a message when the command /help is issued."""
	update.message.reply_text('Utiliza /funfact para leer mis frases.')
	#bot.send_message(chat_id=update.message.chat_id, text="Utiliza /funfact para leer mis frases.")

def error(update, context):
	"""Log Errors caused by Updates."""
	logger.warning('Update "%s" caused error "%s"', update, context.error)

def funFact(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text=randomFact())

def randomFact():
	return random.choice(facts)

def getFacts(filename):
	with open(filename) as facts:
		return list(fact.strip() for fact in facts)

# def funFact(bot, update):
# 	chat_id = update.message.chat_id
# 	text = randomPhrase(data)
# 	bot.send_message(chat_id=chat_id, text=text)

def main():
	TOKEN = os.environ.get('DEMANZANOABOT')
	updater = Updater(TOKEN)
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('start', start))
	dp.add_handler(CommandHandler('help', help))
	dp.add_handler(CommandHandler('funfact', funFact))
	dp.add_error_handler(error)
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	facts = getFacts('facts.txt')
	main()