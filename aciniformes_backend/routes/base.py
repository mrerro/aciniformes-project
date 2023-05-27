from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from aciniformes_backend.settings import get_settings

from .fetcher import router as fetcher_router
from .mectric import router as metric_router

settings = get_settings()
app = FastAPI()

app.add_middleware(
    DBSessionMiddleware,
    db_url=settings.DB_DSN,
)

app.include_router(fetcher_router, prefix='/fetcher')
app.include_router(metric_router, prefix='/metric')
