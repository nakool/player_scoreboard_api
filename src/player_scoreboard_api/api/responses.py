from lib2to3.pytree import Base
from pydantic import BaseModel


class GenericErrorResponse(BaseModel):
    error_code: str
    error_msg: str
