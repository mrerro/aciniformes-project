from sqlalchemy import JSON
from sqlalchemy.orm import Session

from aciniformes_backend.models import Fetcher, FetcherType, ResultType


class FetcherJob:
    fetcher_id: str
    name: str
    type_: FetcherType
    settings: JSON
    delay_sec: int
    result: ResultType
    trigger_timer_sec: float
    db_session: type[Session]

    def __init__(self, fetcher: Fetcher, db_session) -> None:
        self.fetcher_id = fetcher.id_
        self.name = fetcher.name
        self.type_ = fetcher.type_
        self.settings = fetcher.settings
        self.delay_sec = fetcher.delay_sec
        self.result = fetcher.result
        self.trigger_timer_sec = self.delay_sec
        self.db_session = db_session

    # def __eq__(self, other):
    #     if not isinstance(other, FetcherJob):
    #         raise TypeError("Операнд справа должен иметь тип Task")

    #     return self.fetcher_id == other.fetcher_id

    def reconfigure(self, fetcher: Fetcher) -> None:
        self.__init__(fetcher)

    def update(self, sec: float) -> None:
        self.trigger_timer_sec = self.trigger_timer_sec - sec
        if self.trigger_timer_sec <= 0:
            self.trigger_timer_sec = self.delay_sec
            self.__action()

    def __action(self) -> None:
        match self.type_:
            case FetcherType.GET:
                pass
            case FetcherType.POST:
                pass
            case FetcherType.PING:
                pass
