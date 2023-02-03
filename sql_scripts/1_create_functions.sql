CREATE OR REPLACE FUNCTION insert_vacancy_with_skills (
    ext_id       INTEGER,
    vacancy_name VARCHAR,
    published_at TIMESTAMP,
    skill_names  VARCHAR[])
RETURNS void
AS $$
    DECLARE
        current_id vacancies.vacancy_id%type;
    BEGIN
        INSERT INTO vacancies (external_id, vacancy_name, published_at)
        VALUES (ext_id, vacancy_name, published_at)
            ON conflict(external_id) DO nothing
               RETURNING vacancy_id INTO current_id;

        INSERT INTO skills (skill_name)
        SELECT *
          FROM unnest(skill_names)
            ON conflict DO nothing;

        INSERT INTO vacancy_skill (vacancy_id, skill_id)
        SELECT current_id, s.skill_id
          FROM skills s
         WHERE s.skill_name = any(skill_names)
            ON conflict DO nothing;
    END
$$ LANGUAGE PLPGSQL;


CREATE OR REPLACE FUNCTION filter_existing_vacancies(ext_ids INTEGER[])
RETURNS SETOF INTEGER
AS $$
    SELECT param
      FROM unnest(ext_ids) AS param
	  WHERE param NOT IN (SELECT external_id FROM vacancies)
$$ LANGUAGE SQL;


CREATE OR REPLACE FUNCTION rate_skills(
    date_FROM TIMESTAMP,
    date_to   TIMESTAMP)
RETURNS TABLE (
    skill_name VARCHAR,
    rate       SMALLINT)
AS $$
    SELECT s.skill_name,
           COUNT(vs.vacancy_id) AS rate
      FROM skills s
           JOIN vacancy_skill vs
           ON vs.skill_id = s.skill_id
           JOIN vacancies v
           ON v.vacancy_id = vs.vacancy_id
     WHERE v.published_at BETWEEN date_FROM AND date_to
     GROUP BY s.skill_id
    HAVING COUNT(vs.vacancy_id) > 1
     ORDER BY rate DESC;
$$ LANGUAGE SQL;