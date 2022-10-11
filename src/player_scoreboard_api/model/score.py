""" Score Model """
from datetime import datetime
from pydantic import BaseModel, validator

from .game import GameEnum


class Score(BaseModel):
    """ Model to store a score for a specific Game with his timestamp"""
    value: int
    # Define a validator for the value 0 to +infini
    # https://pydantic-docs.helpmanual.io/usage/validators/
    game: GameEnum
    at: datetime

    @validator('value')
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
