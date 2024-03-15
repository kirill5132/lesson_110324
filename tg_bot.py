import pprint

import requests
token ='7037321686:AAFBRtsXC2T7dDuWj4okyhtq2j7ziQHbfoc'
main_url = f'https://api.telegram.org/bot{token}'
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