import logging
import fastapi
from starlette.types import Scope, Receive, Send
from dependency_injector import wiring, providers

from .version import VERSION
from .api import api_router


FASTAPI_EVENT_STARTUP = "startup"
FASTAPI_EVENT_SHUTDOWN = "shutdown"


logger = logging.getLogger(__package__)


class Application:

    name: str = "Player Scoreboard Api"
    description: str = """Player Scoreboard Api"""

    _fastapi: fastapi.FastAPI
    _container = None

    def _init_fastapi(self) -> None:
        self._fastapi = fastapi.FastAPI(
            title=self.name,
            description=self.description,
            version=VERSION
        )

        self._fastapi.add_event_handler(
            event_type=FASTAPI_EVENT_STARTUP,
            func=self._on_startup
        )

        self._fastapi.add_event_handler(
            event_type=FASTAPI_EVENT_SHUTDOWN,
            func=self._on_shutdown
        )

        self._fastapi.include_router(api_router)

    def _init_container(self) -> None:
        from .container import Container
        self._container = Container(
            application=providers.Object(self))

    def __init__(self) -> None:
        self._init_fastapi()
        self._init_container()

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if self._fastapi.root_path:
            scope["root_path"] = self._fastapi.root_path
        await self._fastapi.__call__(scope, receive, send)

    async def _on_startup(self):
        logger.debug("ON_STARTUP")
        #await self._container.init_resources()

    async def _on_shutdown(self):
        logger.debug("ON_SHUTDOWN")
        #await self._container.shutdown_resources()
