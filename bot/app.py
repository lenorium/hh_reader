import time
from datetime import timedelta, datetime

import schedule

import telegram_bot
import crud
from logger import logger
from config import settings


def create_msg_text(skills: dict, date_from: datetime, date_to: datetime) -> str:
    mask = '%d.%m.%Y, %H:%M'
    msg = f'Рейтинг навыков за период\n{date_from.strftime(mask)} - {date_to.strftime(mask)}\n\n'
    rating = '\n'.join(f'{key}: {value}' for key, value in skills.items())
    return msg + rating


def get_skills_rating(date_from: datetime, date_to: datetime):
    return crud.rate_skills(date_from, date_to)


def job_send_rating(date_from, date_to):
    skills = get_skills_rating(date_from, date_to)
    msg = create_msg_text(skills, date_from, date_to)
    telegram_bot.send_message(msg)


if __name__ == '__main__':
    if settings.use_telegram:
        date_to = settings.search_date_to
        date_from = date_to - timedelta(days=settings.send_msg_n_days)

        if settings.run_by_schedule:

            logger.info(f'Формирование списка навыков по расписанию в {settings.send_msg_at} '
                        f'каждые {settings.send_msg_n_days} дня(дней)')

            schedule.every(settings.send_msg_at)\
                .days\
                .at(settings.send_msg_n_days)\
                .do(job_send_rating,
                    date_from=date_from,
                    date_to=date_to)

            while True:
                schedule.run_pending()
                time.sleep(1)
        else:
            job_send_rating(date_from, date_to)
    else:
        logger.info('Отсутствует Telegram API Token')