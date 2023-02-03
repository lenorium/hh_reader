from hh_api import api_methods as api
from models import Vacancy, VacancySearchResult

import config as settings


def get_vacancies(**params) -> list:
    response = api.get(settings.SEARCH_URL + '/vacancies', 200, **params)
    result = VacancySearchResult(response)
    vacancies = []
    for item in result.items:
        vacancies.append(Vacancy(item))
    return vacancies


def get_vacancy_details(_id: int) -> Vacancy:
    response = api.get(settings.SEARCH_URL + '/vacancies/' + str(_id))
    return Vacancy(response)

