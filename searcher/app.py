import time
from datetime import timedelta, datetime

import schedule

from logger import logger
from db import crud as db
from hh_api import vacancies_api
import config as settings


def job_collect_data(date_from: datetime, date_to: datetime):
    page = 0

    while True:
        logger.info(
            f'1. Получаем список вакансий: страница {page} на каждой странице '
            f'{settings.SEARCH_PER_PAGE}\n записей')
        vacancies = vacancies_api.get_vacancies(text=settings.SEARCH_TEXT,
                                                search_field=settings.SEARCH_FIELD,
                                                date_from=date_from.isoformat(),
                                                date_to=date_to.isoformat(),
                                                area=settings.SEARCH_AREA,  # Россия
                                                per_page=settings.SEARCH_PER_PAGE,
                                                page=page,
                                                order_by=settings.SEARCH_ORDER_BY)
        if not vacancies:
            logger.info(f'2. Новых вакансий за выбранный период {date_from} - {date_to} нет\n')
            break

        page += 1

        logger.info('2. Проверяем полученный список вакансий на наличие в БД.\n'
                    'Если такая уже есть, то пропускаем (не обновляем).')
        external_ids = [v.external_id for v in vacancies]
        external_ids = db.filter_if_exists(external_ids)

        logger.info('3. Запрашиваем каждую вакансию для получения списка навыков\n')
        vacancies_full = [vacancies_api.get_vacancy_details(_id) for _id in external_ids]

        # выбираем только те навыки, которые написаны на англ, чтоб не попадали всякие типа "Ответственность"
        for v in vacancies_full:
            v.skills = [s.lower() for s in v.skills if s.isascii()]

        logger.info('4. Сохраняем вакансии с навыками в базу данных\n')
        db.save_vacancies_full(vacancies_full)


if __name__ == '__main__':
    date_to = settings.SEARCH_DATE_TO
    date_from = date_to - timedelta(days=settings.SEARCH_EVERY_N_DAYS)

    if settings.RUN_BY_SCHEDULE:

        logger.info(f'Поиск вакансий по расписанию в {settings.SEARCH_RUN_AT} '
                    f'каждые {settings.SEARCH_EVERY_N_DAYS} дня(дней)')

        schedule.every(settings.SEARCH_EVERY_N_DAYS) \
            .days\
            .at(settings.SEARCH_RUN_AT)\
            .do(job_collect_data,
                date_from=date_from,
                date_to=date_to)

        while True:
            schedule.run_pending()
            time.sleep(1)
    else:
        job_collect_data(date_from, date_to)
