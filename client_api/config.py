import os

from dotenv import load_dotenv

load_dotenv('../.env' if os.path.exists('../.env') else '../.env-shared')

LOG_LEVEL = os.getenv('LOG_LEVEL', default='INFO').upper()

DB_URL = os.getenv('DATABASE_URL')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_LOG = LOG_LEVEL == 'DEBUG'

API_PORT = int(os.getenv('API_PORT'))
