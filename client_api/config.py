import os

from pydantic import BaseSettings, Field


class __Settings(BaseSettings):
    db_url: str = Field(env='DATABASE_URL')
    db_host: str = Field(env='POSTGRES_HOST')
    db_port: str = Field(env='POSTGRES_PORT')
    db_name: str = Field(env='POSTGRES_DB')
    db_user: str = Field(env='POSTGRES_USER')
    db_password: str = Field(env='POSTGRES_PASSWORD')
    api_port: int = Field(env='API_PORT')
    log_level: str = Field(env='LOG_LEVEL')


settings = __Settings(_env_file='../.env' if os.path.exists('../.env') else '../.env-shared')