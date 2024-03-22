import pprint
import telebot
import requests
import random

bot = telebot.TeleBot('token1')

token1 ='7037321686:AAFBRtsXC2T7dDuWj4okyhtq2j7ziQHbfoc'
main_url = f'https://api.telegram.org/bot{token1}'
#url = f'{main_url}/getMe'

#result = requests.get(url)
#print(result.json())

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
    result = requests.post(url,params=params)

@bot.message_handler(commands=['quote'])
def send_welcome(message):
    bot.reply_to(message, 'у сигма сигма')

@bot.message_handler(content_types=['sigma'])
def send_sticker(message):
    print(message)
    file_ID = 'CAACAgEAAxkBAAIBa2X0Zy6kg0p_iIoyXyy5kexA5VmmAAJ-AQACDmEBRASfnE_40iadNAQ'
    bot.send_sticker(message.chat.id,file_ID)

@bot.message_handler(commands=['random'])
def send_random(numbers):
    numbers = random.randint(1,100)
    print(numbers)

bot.polling()
