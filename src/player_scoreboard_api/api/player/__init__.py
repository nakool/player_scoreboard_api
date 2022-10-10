
from http import HTTPStatus
from fastapi import Depends, APIRouter, Response
from dependency_injector.wiring import Provide, inject

from player_scoreboard_api.container import Container
from player_scoreboard_api.service.player_service import PlayerService

player_router = APIRouter()



@player_router.post(
    path="/player/{name}"
)
@inject
def add_player(name: str, player_service: PlayerService = Depends(Provide[Container.player_service])):
    return player_service.add_player(name)


@player_router.get(
    path="/player"
)
@inject
def list_player_name(player_service: PlayerService = Depends(Provide[Container.player_service])):
    return player_service.get_player_list()
