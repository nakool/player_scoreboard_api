from pydantic import BaseModel


class GenericErrorResponse(BaseModel):
    error_code: str
    error_msg: str
