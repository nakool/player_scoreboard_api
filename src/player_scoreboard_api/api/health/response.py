from pydantic import BaseModel

from player_scoreboard_api.service.health import HealthStatus



class HealthResponse(BaseModel):
    status: HealthStatus
