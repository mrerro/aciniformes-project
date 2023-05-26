from __future__ import annotations

import re
from datetime import datetime
from enum import Enum as BaseEnum

from sqlalchemy import JSON, DateTime, Enum, Float, Integer, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean


@as_declarative()
class Model:
    @declared_attr
    def __tablename__(cls) -> str:  # pylint: disable=no-self-argument
        """Generate database table name automatically.
        Convert CamelCase class name to snake_case db table name.
        """
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()


class Metric(Model):
    id_: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    value: Mapped[float] = mapped_column(Float, nullable=False)
    create_ts: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # fetchers: Mapped[list[Fetcher]] = relationship('Fetcher', back_populates='metrics')


class FetcherType(str, BaseEnum):
    GET: str = 'get'
    POST: str = 'post'
    PING: str = 'ping'


class ResultType(str, BaseEnum):
    STATUS_CODE: str = 'status_code'
    CONTENT_LENGTH: str = 'content_length'
    AVAILABLE: str = 'available'


class Fetcher(Model):
    id_: Mapped[int] = mapped_column('id', Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    type_: Mapped[FetcherType] = mapped_column(
        'type', Enum(FetcherType, native_enum=False), nullable=False
    )
    settings: Mapped[JSON] = mapped_column(JSON, default={}, nullable=False)
    delay_sec: Mapped[float] = mapped_column(Float, default=60, nullable=False)
    result: Mapped[ResultType] = mapped_column(Enum(ResultType, native_enum=False), nullable=False)
    create_ts: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    modify_ts: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    # metrics: Mapped[list[Metric]] = relationship('Metric', back_populates='fetchers')
