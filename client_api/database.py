from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import config as settings

if settings.DB_URL:
    connect_url = settings.DB_URL
else:
    connect_url = {
        'drivername': 'postgresql+psycopg2',
        'host': settings.DB_HOST,
        'port': settings.DB_PORT,
        'username': settings.DB_USER,
        'password': settings.DB_PASSWORD,
        'database': settings.DB_NAME
    }
    connect_url = URL(**connect_url)

Base = automap_base()
engine = create_engine(connect_url, echo=settings.DB_LOG)
session_maker = sessionmaker(bind=engine)
Base.prepare(autoload_with=engine)