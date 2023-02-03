# Hard Skills Parser (HeadHunter)

Парсер для подсчета упоминаемости хард скиллов в вакансиях на сайте [HeadHunter](https://hh.ru/).

## Для чего полезен

Составляет список наиболее часто упоминаемых в требованиях навыков.
Такой список помогает сориентироваться, какой стек технологий необходимо знать/изучать для работы или развития в выбранном направлении. 


## Как работает

Просматривает свежие вакансии на заданную специальность за указанный период, собирает из каждой из них список требуемых
навыков в разделе "Ключевые навыки" (пример такого раздела на скрине ниже),  
фильтрует полученный список таким образом, чтобы исключить упоминания софт скиллов (вроде "Аналитическое мышление") и из остальных
составляет рейтинг упоминаемости по убыванию. 

<details>
  <summary>Пример ключевых навыков на hh</summary>
    
![Image alt](https://github.com/lenorium/images_for_readme/blob/main/key_skills.png)
    
</details>

Проект был создан для собственного пользования, находится на хостинге, работает по расписанию и
собирает вакансии по одной выбранной специальности. Но также предусмотрена возможность запустить в Docker-контейнере (чтобы просто посмотреть как работает). 
Об этом в блоке [демо](#демо).

## Структура


## Демо

Ниже приведено описание, как запустить в Docker-контейнере.

1. У вас должен быть установлен [Docker](https://www.docker.com/products/docker-desktop/)
2. Склонировать проект
3. В терминале/консоли, находясь в папке с проектом (```<path>/hh_reader/```), запустить контейнеры
    
    ```bash
    docker-compose up -d
    ```
4. Подождать, когда все поднимется. В логах докера можно будет увидеть, что начался парсинг hh и сбор информации о вакансиях.
5. В браузере перейти по адресу http://0.0.0.0:8000/ или http://127.0.0.1:8000/ (что более вероятно, если у вас Safari). 
Если все работает, вы это поймете без дополнительных комментариев. если нет - тоже.
6. Перейти на http://0.0.0.0:8000/docs для открытия документации в Swagger. Там должно быть все понятно.

**Дополнительно**

Структуру БД можно посмотреть перейдя по адресу http://0.0.0.0:8001/ (или http://127.0.0.1:8001/) в PGAdmin-е. 
1. Логин и пароль для авторизации указаны в файле ```.env-shared```. 
2. Далее, когда откроется дашборд, нажать на ```Add New Server```. 
3. В качестве имени сервера указать любое на свое усмотрение, во вкладке Connection в поле ```Host``` указать ```db```. 
Пароль все тот же.
5. Если все хорошо, должен открыться список баз данных, среди которых будет искомая. 


### Конфиги

Все изменяемые параметры вынесены в файл конфигураций .env-shared. 
Всем использумым в этом файле переменным заданы значения по умолчанию. Но также их можно менять.
Ниже приведено описание. 

|Имя переменной|Назначение|Возможные значения|
|--------------|----------|---|
|SEARCH_TEXT| Название интересующей специальности| Любое название специальности. Без кавычек|
|SEARCH_FIELD| Область поиска. Определяет, где hh будет искать вхождения текста в переменной (в названии вакансии, в описании или в названии компании)|```name, company_name, description```. Согласно [документации API HH](https://api.hh.ru/openapi/redoc#tag/Obshie-spravochniki/paths/~1dictionaries/get)|
|SEARCH_AREA| Регион поиска (страна, горд и тд)| Возможные значения описаны в [справочнике регионов API HH](https://api.hh.ru/areas)|
|SEARCH_PER_PAGE| Количество результатов на одной странице| Не более 100|
|SEARCH_ORDER_BY| Сортировка списка вакансий| ```publication_time, salary_desc, salary_asc, relevance, distance```. [Документация API HH](https://api.hh.ru/openapi/redoc#tag/Obshie-spravochniki/paths/~1dictionaries/get)|
|SEARCH_DATE_TO| Дата, до которой искать вакансии| В формате ```%Y-%m-%d```. Если оставить пустым, то берется текущая дата| 
|RUN_BY_SCHEDULE| Запускать ли по расписанию| True, False|
|SEARCH_RUN_AT| Время запуска поиска вакансий (если используется расписание)| Время в формате ```HH:mm```|
|SEARCH_EVERY_N_DAYS| Запускать поиск вакансий каждые ... дней| Целое число|
|SEND_MSG_AT| Время составления списка навыков и отправки сообщения| Время в формате ```HH:mm```|
|SEND_MSG_EVERY_N_DAYS|Присылать сообщение со списком навыков каждые ... дней| Целое число|

## Используемый стек
- Python 3.10 (SQLAlchemy, FastAPI)
- SQL
- PostgresQL
- Docker
- PGAdmin

## Следующие шаги
1. Добавить обработку исключений
2. Вынести повторяющиеся фрагменты кода
