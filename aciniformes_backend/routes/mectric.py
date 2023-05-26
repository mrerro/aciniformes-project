from datetime import datetime

from fastapi import APIRouter
from fastapi_sqlalchemy import db
from pydantic import BaseModel, Field

from aciniformes_backend.models import Metric


class CreateSchema(BaseModel):
    name: str = Field(description='Название метрики', example='Терминал принтера')
    value: float = Field(description='Значение', example=1)
    create_ts: datetime = Field(description='Время создания метрики', example=datetime.utcnow())


# class UpdateSchema(BaseModel):
#     pass


# class GetSchema(BaseModel):
#     id: int


router = APIRouter()


@router.post('')
def create(inp: CreateSchema):
    file_model = Metric(name=inp.name, value=inp.value)
    if inp.create_ts is not None:
        file_model.create_ts = inp.create_ts
    db.session.add(file_model)
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
