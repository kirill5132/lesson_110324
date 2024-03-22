import telebot
import random

token = '7037321686:AAFBRtsXC2T7dDuWj4okyhtq2j7ziQHbfoc'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['quote'])
def send_welcome(message1):
    bot.reply_to(message1, 'у сигма сигма')


@bot.message_handler(commands=['sigma'])
def send_sticker(message1):
    print(message1)
    file_id = 'CAACAgEAAxkBAAIBa2X0Zy6kg0p_iIoyXyy5kexA5VmmAAJ-AQACDmEBRASfnE_40iadNAQ'
    bot.send_sticker(message1.chat.id, file_id)


@bot.message_handler(commands=['random'])
def send_random():
    numbers = random.randint(1, 100)
    print(numbers)


@bot.message_handler(commands=['audio'])
def send_audio(message1):
    print(message1)
    open("argenby-sigma-iz-tik-toka.mp3", 'rb')
    bot.send_audio(message1.chat.id, "AgADIksAArST8Es")


bot.polling()
