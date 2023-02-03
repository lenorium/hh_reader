import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv('../.env' if os.path.exists('../.env') else '../.env-shared')

RUN_BY_SCHEDULE = os.getenv('RUN_BY_SCHEDULE', False) == 'True'

SEND_MSG_EVERY_N_DAYS = int(os.getenv('SEND_MSG_EVERY_N_DAYS', default=1))
SEND_MSG_AT = os.getenv('SEND_MSG_AT', '10:10')

LOG_LEVEL = os.getenv('LOG_LEVEL', default='INFO').upper()

DB_URL = os.getenv('DATABASE_URL')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_LOG = LOG_LEVEL == 'DEBUG'

TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
USE_TELEGRAM = TELEGRAM_API_TOKEN is not None

