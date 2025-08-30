import telebot
from base import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    print (chat_id)
    bot.send_message(chat_id=chat_id, text='Ваш ID: '+str(chat_id))

bot.polling()