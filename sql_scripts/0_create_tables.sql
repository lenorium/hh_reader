CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id    SERIAL        PRIMARY KEY,
    vacancy_name  VARCHAR(120),
    published_at  TIMESTAMP,
    external_id   INTEGER       UNIQUE
);

CREATE TABLE IF NOT EXISTS skills (
    skill_id    SERIAL      PRIMARY KEY,
    skill_name  VARCHAR(50) UNIQUE
);

CREATE TABLE IF NOT EXISTS vacancy_skill (
    vacancy_id INTEGER  REFERENCES vacancies (vacancy_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE,
    skill_id   INTEGER  REFERENCES skills (skill_id)
                        ON UPDATE CASCADE
                        ON DELETE CASCADE,
    UNIQUE (vacancy_id, skill_id)
);
