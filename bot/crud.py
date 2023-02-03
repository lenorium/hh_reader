from datetime import datetime

from sqlalchemy import text

from database import session_maker


def rate_skills(date_from: datetime, date_to: datetime) -> dict:
    with session_maker() as session:
        statement = text(f'''select * from rate_skills('{date_from}', '{date_to}')''')
        result = session.execute(statement).all()
        return dict(result)

