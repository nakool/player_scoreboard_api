""" Input object for player api"""
from datetime import datetime
from pydantic import BaseModel, validator

from ...model.game import GameEnum


class ScoreInput(BaseModel):
    """ Input Model for the Body definition of add player score """
    score: int
    game: GameEnum
    at = datetime


    @validator('score')
    def value_more_equal(cls, v):
        """
        :param cls: str classname here Score
        :param v: int actual value of "value"

        YOU CAN USE THE DEBUGGER TO UNDESTAND WHAT IS USE :)
        """
        if v >= 0:
            return v
        else:
            raise ValueError("Score value need to be more or equal to 0")