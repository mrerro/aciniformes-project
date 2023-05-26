import sqlalchemy
from sqlalchemy.orm import sessionmaker

from aciniformes_backend.models import Fetcher
from aciniformes_backend.settings import get_settings
from aciniformes_backend.fetcher_job import FetcherJob


settings = get_settings()


class Scheduler:
    db: sqlalchemy.Engine
    fetchers: list[Fetcher]
    fetcher_jobs: list[FetcherJob]
    update_fetcher_job_delay_sec: int
    trigger_timer_sec: float

    def __init__(self) -> None:
        self.db = sqlalchemy.create_engine(settings.DB_DSN)
        self.fetchers = self.db.query(Fetcher).all() #FIXME WRONG
        self.fetcher_jobs = []
        for fetcher in self.fetchers:
            self.fetcher_jobs.append(FetcherJob(fetcher, sessionmaker(self.db)))
        self.update_fetcher_job_delay_sec = settings.SCHEDULER_UPDATE_FETCHER_JOB_SEC
        self.trigger_timer_sec = self.update_fetcher_job_delay_sec

    def update(self, sec: float) -> None:
        self.__upgrade_fetcher_jobs(sec)
        for job in self.fetcher_jobs:
            job.update(sec)

    def __upgrade_fetcher_jobs(self, sec: float):
        self.trigger_timer_sec = self.trigger_timer_sec - sec
        if self.trigger_timer_sec <= 0:
            self.trigger_timer_sec = self.update_fetcher_job_delay_sec
            # TODO актуализация jobs
