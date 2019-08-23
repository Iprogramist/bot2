token='841827830:AAGsY5L9zmtZvq8DbkEuaTh9KVqnJkTfc-M'
import telebot
from telebot.types import Message

bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def geo_t(message: Message):
    bot.send_message(message.chat.id,text='Прив')
bot.polling()

