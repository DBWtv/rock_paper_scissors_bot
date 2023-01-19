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
            requests.get(
                f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

            time.sleep(1)
            counter += 1