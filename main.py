import telebot
from dotenv import load_dotenv
import os

bot = telebot.TeleBot(os.getenv('TOKEN'), parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def start(message):
     bot.send_message(message.chat.id, '/start')

bot.polling()