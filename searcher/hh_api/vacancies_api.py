from hh_api import api_methods as api
from models import Vacancy, VacancySearchResult

from config import settings


def get_vacancies(**params) -> list:
    response = api.get(settings.search_url + '/vacancies', 200, **params)
    result = VacancySearchResult(response)
    vacancies = []
    for item in result.items:
        vacancies.append(Vacancy(item))
    return vacancies


def get_vacancy_details(_id: int) -> Vacancy:
    response = api.get(settings.search_url + '/vacancies/' + str(_id))
    return Vacancy(response)

