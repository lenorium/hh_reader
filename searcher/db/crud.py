from db.database import session_maker


def filter_if_exists(external_ids: list[int]) -> list[int]:
    with session_maker() as session:
        result = session.execute(func.public.filter_existing_vacancies(external_ids)).all()
    return [item for sublist in result for item in sublist]


def save_vacancies_full(data: list[Vacancy]):
    with session_maker.begin() as session:
        for line in data:
            session.execute(
                func.public.insert_vacancy_with_skills(
                    line.external_id,
                    line.vacancy_name,
                    line.published_at,
                    line.skills)
            ).all()
