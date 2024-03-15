import telebot
import time

token ='7037321686:AAFBRtsXC2T7dDuWj4okyhtq2j7ziQHbfoc'


bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Как твои дела?Чем я могу помочь тебе')

@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(commands=['say'])
def say(message):
    text = ''.join(message.text.split('')[1:])
    bot.reply_to((message,f'***{text.upper()}!***'))

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgEAAxkBAAIBa2X0Zy6kg0p_iIoyXyy5kexA5VmmAAJ-AQACDmEBRASfnE_40iadNAQ'
    bot.send_sticker(message.chat.id,file_ID)

@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'плохой' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово плохой')
        return
    #text = message.text[::-1]
    text = message.text[::1]
    bot.reply_to(message, text)


bot.polling()
