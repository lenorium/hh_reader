import time
from datetime import timedelta, datetime

import schedule

import config as settings
import crud
import telegram_bot
from logger import logger


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
    if settings.USE_TELEGRAM:
        date_to = datetime.now()
        date_from = date_to - timedelta(days=settings.SEND_MSG_EVERY_N_DAYS)

        date_from = datetime.combine(date_from, datetime.min.time())
        date_to = datetime.combine(date_to, datetime.max.time())

        if settings.RUN_BY_SCHEDULE:

            logger.info(f'Формирование списка навыков по расписанию в {settings.SEND_MSG_AT} '
                        f'каждые {settings.SEND_MSG_EVERY_N_DAYS} дня(дней)')

            schedule.every(settings.SEND_MSG_EVERY_N_DAYS) \
                .days\
                .at(settings.SEND_MSG_AT)\
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