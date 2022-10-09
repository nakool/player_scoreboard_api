
from http import HTTPStatus
import pydantic
from fastapi import Depends, APIRouter, Response
from dependency_injector.wiring import Provide, inject

from player_scoreboard_api.container import Container
from player_scoreboard_api.service.health import HealthService, HealthStatus
from .response import HealthResponse

health_router = APIRouter()





@health_router.get(
    path="/health",
    responses={
        HTTPStatus.OK.value: {"model": HealthResponse},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {"model": HealthResponse}
    }
)
@inject
def get_health(response: Response, health_service: HealthService = Depends(Provide[Container.health_service])):
    _status = health_service.get_status()
    if _status == HealthStatus.OK:
        response.status_code = HTTPStatus.OK
        return HealthResponse(status=_status)
    else:
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return HealthResponse(status=_status)
