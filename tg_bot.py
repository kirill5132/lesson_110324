import pprint
import telebot
import requests
import random

bot = telebot.TeleBot('token1')

token1 = '7037321686:AAFBRtsXC2T7dDuWj4okyhtq2j7ziQHbfoc'
main_url = f'https://api.telegram.org/bot{token1}'

url = f'{main_url}/getUpdates'
result = requests.get(url)
pprint.pprint(result.json())

messages = result.json()['result']
for message in messages:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': 'Привет дорогой пользователь'
    }
    result = requests.post(url, params=params)


@bot.message_handler(commands=['quote'])
def send_welcome(message1):
    bot.reply_to(message1, 'у сигма сигма')


@bot.message_handler(content_types=['sigma'])
def send_sticker(message1):
    print(message1)
    file_id = 'CAACAgEAAxkBAAIBa2X0Zy6kg0p_iIoyXyy5kexA5VmmAAJ-AQACDmEBRASfnE_40iadNAQ'
    bot.send_sticker(message1.chat.id, file_id)


@bot.message_handler(commands=['random'])
def send_random():
    numbers = random.randint(1, 100)
    print(numbers)

@bot.message_handler(commands=['audio'])
def send_audio():
    audio = open("argenby-sigma-iz-tik-toka.mp3", 'rb')
    bot.send_audio(message.chat.id, "AgADIksAArST8Es")


bot.polling()
