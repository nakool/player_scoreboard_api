from fastapi import APIRouter


API_ROUTER_PREFIX = "/api"

api_router = APIRouter(
    prefix=API_ROUTER_PREFIX
)