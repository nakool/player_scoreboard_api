from fastapi import APIRouter


from .health import health_router
from .player import player_router


API_ROUTER_PREFIX = "/api"

api_router = APIRouter(
    prefix=API_ROUTER_PREFIX
)
api_router.include_router(health_router)
api_router.include_router(player_router)
