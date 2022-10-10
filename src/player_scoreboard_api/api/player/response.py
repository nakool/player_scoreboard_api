from typing import List
from pydantic import BaseModel


class PlayerAddResponse(BaseModel):
    added: bool
    name: str


class PlayerListResponse(BaseModel):
    players: List[str]
