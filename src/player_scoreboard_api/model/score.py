from pydantic import BaseModel
from datetime import datetime

from .game import GameEnum


class Score(BaseModel):
    value: int
    game: GameEnum
    at: datetime
