from pydantic import BaseModel
from datetime import datetime
from typing import List

from .score import Score


class Player(BaseModel):
    name: str
    date_creation: datetime
    score_list: List[Score]
