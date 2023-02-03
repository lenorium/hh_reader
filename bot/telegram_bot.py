import api_methods
import config as settings


def send_message(message):
    api_url = f'https://api.telegram.org/bot{settings.TELEGRAM_API_TOKEN}/sendMessage'

    api_methods.post(api_url, json={'chat_id': settings.TELEGRAM_CHAT_ID, 'text': message}, code=200)
