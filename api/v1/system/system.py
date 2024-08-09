from fastapi import APIRouter

from app.schemas.responses.common import MessageResponse


system_router = APIRouter(tags=["System"])


@system_router.get(
    "/ping",

)
async def ping() -> MessageResponse:
    return MessageResponse(message="pong")


@system_router.get("/error")
async def error() -> MessageResponse:
    from core.exceptions.base import NotFoundException
    raise NotFoundException("Fuck")
    return MessageResponse(message="fuck")

