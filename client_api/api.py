from datetime import timedelta, datetime, date

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import config as settings
import crud
from database import session_maker

app = FastAPI()


def get_session():
    with session_maker() as session:
        yield session


@app.get('/')
def home():
    return 'It works!'


@app.get('/skills')
def skills(session: Session = Depends(get_session),
           date_from: date = date.today() - timedelta(days=1),
           date_to: date = date.today()):
    date_from = datetime.combine(date_from, datetime.min.time())
    date_to = datetime.combine(date_to, datetime.max.time())
    return crud.rate_skills(session, date_from, date_to)


if __name__ == '__main__':
    uvicorn.run("api:app", host='0.0.0.0', port=settings.API_PORT, log_level=settings.LOG_LEVEL.lower(), reload=True)
