from fastapi import APIRouter
from fastapi_sqlalchemy import db
from pydantic import BaseModel, Field

from aciniformes_backend.models import Fetcher, FetcherType, ResultType


class CreateSchema(BaseModel):
    name: str = Field(description='Название метрики', example='Терминал принтера')
    type_: FetcherType = Field(description='Тип запроса', example=FetcherType.GET)
    settings: dict = Field(description='Настройки запроса', example={})
    delay_sec: int = Field(description='Частота проверки', example=30)
    result: ResultType = Field(description='Тип результата', example=ResultType.AVAILABLE)


# class UpdateSchema(BaseModel):
#     pass


# class GetSchema(BaseModel):
#     id: int


router = APIRouter()


@router.post('')
def create(inp: CreateSchema):
    fetcher_model = Fetcher(
        name=inp.name, type_=inp.type_, settings=inp.settings, delay_sec=inp.delay_sec, result=inp.result
    )
    db.session.add(fetcher_model)
    db.session.commit()


# @router.get('')
# def get_all():
#     pass


# @router.get("/{id}")
# def get(id: int):
#     pass


# @router.patch("/{id}")
# def update(id: int):
#     pass


# @router.delete("/{id}")
# def delete(id: int):
#     pass
