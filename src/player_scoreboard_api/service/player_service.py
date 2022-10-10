import logging
from select import select
from typing import Dict, List

logger = logging.getLogger(__package__)


class PlayerService():

    players: Dict[str, str]

    def __init__(self) -> None:
        logger.info("Scoreboard Player Name")
        self.players = dict()

    def add_player(self, name: str) -> bool:
        self.players[name] = name
        return True

    def get_player(self, name: str) -> str | None:
        return self.players.get(name, None)

    def get_player_list(self) -> List[str]:
        return list(self.players.keys())