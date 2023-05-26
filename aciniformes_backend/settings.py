from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    DB_DSN: PostgresDsn = 'postgresql://postgres@localhost:5432/postgres'
    SCHEDULER_FREQUENCY_SEC: float = 1
    SCHEDULER_UPDATE_FETCHER_JOB_SEC: float = 2

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
