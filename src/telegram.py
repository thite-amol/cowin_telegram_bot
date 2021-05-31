import requests


def to_telegram(msg):
    token = ""  # bot id
    chat_id = ""  # your group id
    text_to_send = msg
    telegram_url = "https://api.telegram.org/bot"
    temp = telegram_url + token + "/sendMessage?chat_id=" + chat_id + "&text=" + text_to_send
    requests.get(temp)
