import os
from datetime import datetime

from pydantic import BaseSettings, Field, validator


class __Settings(BaseSettings):
    db_url: str = Field(env='DATABASE_URL')
    db_host: str = Field(env='POSTGRES_HOST')
    db_port: str = Field(env='POSTGRES_PORT')
    db_name: str = Field(env='POSTGRES_DB')
    db_user: str = Field(env='POSTGRES_USER')
    db_password: str = Field(env='POSTGRES_PASSWORD')
    api_port: int = Field(env='API_PORT')
    log_level: str = Field(env='LOG_LEVEL')

    search_url: str = Field(env='SEARCH_URL')
    search_text: str = Field(env='SEARCH_TEXT')
    search_field: str = Field(env='SEARCH_FIELD')
    search_area: int = Field(env='SEARCH_AREA')
    search_per_page: int = Field(env='SEARCH_PER_PAGE')
    search_order_by: str = Field(env='SEARCH_ORDER_BY')
    search_date_to: datetime = Field(env='SEARCH_DATE_TO')

    run_by_schedule: bool = Field(env='RUN_BY_SCHEDULE')
    search_every_n_days: int = Field(env='SEARCH_EVERY_N_DAYS')
    search_run_at: str = Field(env='SEARCH_RUN_AT')

    class Config:
        validate_assignment = True

    @validator('log_level')
    def set_log_level(cls, log_level):
        return log_level or 'info'

    @validator('search_area')
    def set_search_area(cls, search_area):
        return search_area or 113 # Если не задано значение, то ищем по всей России (id = 113)

    @validator('search_per_page')
    def set_search_per_page(cls, search_per_page):
        return search_per_page or 10

    @validator('search_date_to')
    def set_search_date_to(cls, search_date_to):
        return search_date_to or datetime.now()

    @validator('run_by_schedule')
    def set_run_by_schedule(cls, run_by_schedule):
        return run_by_schedule or False

    @validator('search_every_n_days')
    def set_search_every_n_days(cls, search_every_n_days):
        return search_every_n_days or 1

    @validator('search_run_at')
    def set_search_run_at(cls, search_run_at):
        return search_run_at or '10:00'


settings = __Settings(_env_file='../.env' if os.path.exists('../.env') else '../.env-shared')