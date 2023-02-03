class Vacancy:
    external_id = None
    vacancy_name = None
    published_at = None
    skills = []

    def __init__(self, attrs: dict):
        super().__init__()
        for key in attrs:
            if key in type(self).__dict__:
                setattr(self, key, attrs[key])
            elif key == 'id':
                self.external_id = int(attrs[key])
            elif key == 'name':
                self.vacancy_name = attrs[key]
            if key == 'key_skills':
                self.skills = [item['name'] for item in attrs[key]]


class VacancySearchResult:
    def __init__(self, attrs: dict):
        self.items = attrs.get('items', [])
