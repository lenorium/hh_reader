from datetime import datetime

from sqlalchemy import text
from sqlalchemy.orm import Session


def rate_skills(session: Session, date_from: datetime, date_to: datetime) -> dict:
    statement = text(f'''select * from rate_skills('{date_from}', '{date_to}')''')
    result = session.execute(statement).all()
    return dict(result)
