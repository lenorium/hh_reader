import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv('../.env' if os.path.exists('../.env') else '../.env-shared')

RUN_BY_SCHEDULE = os.getenv('RUN_BY_SCHEDULE', False) == 'True'

SEARCH_EVERY_N_DAYS = int(os.getenv('SEARCH_EVERY_N_DAYS', default=1))
SEARCH_RUN_AT = os.getenv('SEARCH_RUN_AT', '10:00')

LOG_LEVEL = os.getenv('LOG_LEVEL', default='INFO').upper()

DB_URL = os.getenv('DATABASE_URL')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_LOG = LOG_LEVEL == 'DEBUG'


SEARCH_URL = os.getenv('SEARCH_URL')
SEARCH_TEXT = os.getenv('SEARCH_TEXT')
SEARCH_FIELD = os.getenv('SEARCH_FIELD')
SEARCH_AREA = int(os.getenv('SEARCH_AREA', default=113))  # Если не задано значение, то ищем по всей России (id = 113)
SEARCH_PER_PAGE = int(os.getenv('SEARCH_PER_PAGE', default=10))
SEARCH_ORDER_BY = os.getenv('SEARCH_ORDER_BY')
SEARCH_DATE_TO = os.getenv('SEARCH_DATE_TO')
SEARCH_DATE_TO = datetime.strptime(SEARCH_DATE_TO, '%Y-%m-%d %H:%M:%S') if SEARCH_DATE_TO else datetime.now()

