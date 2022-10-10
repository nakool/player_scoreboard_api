from datetime import datetime
import logging
from typing import Dict, List

from ..model.player import Player

logger = logging.getLogger(__package__)


class PlayerService():

    players: Dict[str, Player]

    def __init__(self) -> None:
        logger.info("Scoreboard Player Name")
        self.players = dict()

    def add_player(self, name: str) -> bool:
        if self.players.get(name, None) is None:
            self.players[name] = Player(
                name=name,
                date_creation=datetime.now(),
                score_list=list()
            )
            return True
        else:
            return False

    def get_player(self, name: str) -> Player | None:
        return self.players.get(name, None)

    def get_player_list(self) -> List[str]:
        return list(self.players.keys())
