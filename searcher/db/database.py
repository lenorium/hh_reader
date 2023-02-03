from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from config import settings

if settings.db_url:
    connect_url = settings.db_url
else:
    connect_url = {
        'drivername': 'postgresql+psycopg2',
        'host': settings.db_host,
        'port': settings.db_port,
        'username': settings.db_user,
        'password': settings.db_password,
        'database': settings.db_name
    }
    connect_url = URL(**connect_url)

echo = settings.log_level == 'debug'
Base = automap_base()
engine = create_engine(connect_url, echo=echo)
session_maker = sessionmaker(bind=engine)
Base.prepare(autoload_with=engine)
