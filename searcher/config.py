import os
from datetime import datetime, timedelta, date

from dotenv import load_dotenv

load_dotenv('../.env' if os.path.exists('../.env') else '../.env-shared')

RUN_BY_SCHEDULE = os.getenv('RUN_BY_SCHEDULE', True) == 'True'

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

__search_date_to = os.getenv('SEARCH_DATE_TO')
__search_date_to = datetime.strptime(__search_date_to, '%Y-%m-%d') if __search_date_to else date.today()
SEARCH_DATE_TO = datetime.combine(__search_date_to, datetime.max.time())

__search_date_from = SEARCH_DATE_TO - timedelta(days=SEARCH_EVERY_N_DAYS)
SEARCH_DATE_FROM = datetime.combine(__search_date_from, datetime.min.time())


