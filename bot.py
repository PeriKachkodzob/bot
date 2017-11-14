import requests
from time import sleep

url = 'https://api.telegram.org/bot319595798:AAFwkNFWi-yfz_bHkicmISilO4MTMo4rRHo/'

def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        _last_update = last_update(get_updates_json(url))
        if update_id == _last_update['update_id']:
            text = _last_update['message']['text']
            chat_id = _last_update['message']['chat']['id']
            send_mess(chat_id, text)
            update_id += 1
        sleep(5)       
main()
