from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

import core.exceptions.base
from api import router
from core.middlewares.middlewares import XProcessTimeMiddleware
# from core.middlewares.exchandlers import HTTPErrorExceptionHandler


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router, prefix="/api")


# def init_exchandlers(app_: FastAPI) -> None:
#     app_.add_exception_handler(core.exceptions.base.HTTPError, HTTPErrorExceptionHandler.handle)
#

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


async def on_startup():
    pass


async def on_shutdown():
    pass


@asynccontextmanager
async def lifespan(app_: FastAPI):
    await on_startup()
    yield
    await on_shutdown()


def create_app() -> FastAPI:
    app_ = FastAPI(lifespan=lifespan)
    init_routers(app_)
    # init_exchandlers(app_)
    init_middlewares(app_)
    return app_


app = create_app()
