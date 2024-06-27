from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import core.exceptions.base
from api import router
from core.middlewares.middlewares import XProcessTimeMiddleware
from core.middlewares.exchandlers import HTTPErrorExceptionHandler


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router, prefix="/api")


def init_exchandlers(app_: FastAPI) -> None:
    app_.add_exception_handler(core.exceptions.base.HTTPError, HTTPErrorExceptionHandler.handle)


def init_middlewares(app_: FastAPI) -> None:
    app_.add_middleware(XProcessTimeMiddleware)
    app_.add_middleware(
        CORSMiddleware,
        **{
            "allow_origins": ["*"],
            "allow_credentials": True,
            "allow_methods": ["*"],
            "allow_headers": ["*"],
        }
    )


def create_app() -> FastAPI:
    app_ = FastAPI()
    init_routers(app_)
    init_exchandlers(app_)
    init_middlewares(app_)
    return app_


app = create_app()


async def init_models():
    from app import models  # ignore unused import statement warning
    from core.database.base import Base
    from core.database.session import engine
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # uncomment it if you want to drop the database. AT YOUR RISK!!!
        await conn.run_sync(Base.metadata.create_all)


async def init_database():
    await init_models()


@app.on_event("startup")
async def on_startup():
    await init_database()


@app.on_event("shutdown")
async def on_shutdown():
    pass
