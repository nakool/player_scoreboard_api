import enum
import logging


logger = logging.getLogger(__package__)


class HealthStatus(str, enum.Enum):
    OK = "OK"
    KO = "KO"


class HealthService():

    status: HealthStatus

    def __init__(self) -> None:
        logger.info("INIT HEALTH SERVICE")
        self.status = HealthStatus.OK

    def get_status(self) -> HealthStatus:
        return self.status
