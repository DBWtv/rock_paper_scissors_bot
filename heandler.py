import requests
import time
from acces_token import token

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = token
TEXT: str = 'Hello there General Kenobi!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:
    print(f'attempt = {counter}')
    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset+1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            photo_url = requests.get('https://aws.random.cat/meow')
            if photo_url.status_code == 200:
                cat_photo_url = photo_url.json()['file']
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_photo_url}')
            else:
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Не получилсоь, не фартануло')

            time.sleep(1)
            counter += 1
