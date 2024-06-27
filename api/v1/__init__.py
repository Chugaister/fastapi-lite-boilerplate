from fastapi import APIRouter

from api.v1.system.system import system_router


v1_router = APIRouter()
v1_router.include_router(system_router, prefix="/system")
