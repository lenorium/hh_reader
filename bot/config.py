import os

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
    run_by_schedule: bool = Field(env='RUN_BY_SCHEDULE')
    send_msg_at: str = Field(env='SEND_MSG_AT')
    send_msg_n_days: int = Field(env='SEND_MSG_EVERY_N_DAYS')

    tg_api_token: str = Field(env='TELEGRAM_API_TOKEN')
    tg_chat_id: str = Field(env='TELEGRAM_CHAT_ID')
    use_telegram = True if tg_api_token else False

    @validator('run_by_schedule')
    def set_run_by_schedule(cls, run_by_schedule):
        return run_by_schedule or False

    @validator('send_msg_n_days')
    def set_send_msg_n_days(cls, send_msg_n_days):
        return send_msg_n_days or 1

    @validator('send_msg_at')
    def set_send_msg_at(cls, send_msg_at):
        return send_msg_at or '10:00'


settings = __Settings(_env_file='../.env' if os.path.exists('../.env') else '../.env-shared')
