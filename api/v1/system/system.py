from fastapi import APIRouter
from fastapi import HTTPException

from app.schemas.responses.common import MessageResponse
from core.exceptions.base import *


system_router = APIRouter(tags=["System"])


@system_router.get(
    "/ping"
)
async def ping() -> MessageResponse:
    return MessageResponse(message="pong")


@system_router.get("/error")
async def error() -> MessageResponse:
    raise BadRequestException("Bad request")
    return MessageResponse(message="message")
