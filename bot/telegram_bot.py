import api_methods
from config import settings


def send_message(message):
    api_url = f'https://api.telegram.org/bot{settings.tg_api_token}/sendMessage'

    api_methods.post(api_url, json={'chat_id': settings.tg_chat_id, 'text': message}, code=200)
