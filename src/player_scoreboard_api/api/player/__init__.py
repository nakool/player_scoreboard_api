
from audioop import add
from http import HTTPStatus
import http
from fastapi import Depends, APIRouter, Response, Path
from dependency_injector.wiring import Provide, inject

from player_scoreboard_api.container import Container
from player_scoreboard_api.service.player import PlayerService

from .response import PlayerAddResponse, PlayerListResponse
from ..responses import GenericErrorResponse
from ...model.player import Player

player_router = APIRouter()

PLAYER_NAME_MIN_LENGTH = 4
PLAYER_NAME_MAX_LENGTH = 32


@player_router.post(
    path="/player/{name}",
    status_code=HTTPStatus.CREATED,
    responses={
        HTTPStatus.CREATED.value: {"model": PlayerAddResponse},
        HTTPStatus.CONFLICT.value: {"model": PlayerAddResponse},
        HTTPStatus.INTERNAL_SERVER_ERROR.value: {"model": GenericErrorResponse}
    }
)
@inject
def add_player(
        response: Response,
        name: str = Path(min_length=PLAYER_NAME_MIN_LENGTH,
                         max_length=PLAYER_NAME_MAX_LENGTH,
                         regex="^[A-Za-z]{3}[A-Za-z0-9]+$"),
        player_service: PlayerService = Depends(Provide[Container.player_service])):
    """
        Controller Endpoint as roles:
        - define the path and parameters
        - validate the format
        - call the "functional service"
        - format the result depending of the result
    """
    try:
        _success = player_service.add_player(name)
    except RuntimeError:
        response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR
        return GenericErrorResponse(
            error_code="",
            error_msg=""
        )
    else:
        if _success:
            response.status_code = HTTPStatus.CREATED
        else:
            response.status_code = HTTPStatus.CONFLICT
        return PlayerAddResponse(added=_success, name=name)


@ player_router.get(
    path="/player"
)
@ inject
def list_player_name(player_service: PlayerService = Depends(Provide[Container.player_service])):
    return PlayerListResponse(players=player_service.get_player_list())


@ player_router.get(
    path="/player/{name}",
    responses={
        HTTPStatus.OK.value: {"model": Player},
        HTTPStatus.NOT_FOUND: {"model": GenericErrorResponse}
    }
)
@ inject
def list_player_name(response: Response,
                     name: str = Path(min_length=PLAYER_NAME_MIN_LENGTH,
                                      max_length=PLAYER_NAME_MAX_LENGTH,
                                      regex="^[A-Za-z]{3}[A-Za-z0-9]+$"), player_service: PlayerService = Depends(Provide[Container.player_service])):
    _player = player_service.get_player(name=name)
    if _player is None:
        response.status_code = HTTPStatus.NOT_FOUND
        return GenericErrorResponse(error_code="404", error_msg="Player don't exist.")
    else:
        response.status_code = HTTPStatus.OK
        return _player
