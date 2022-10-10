from dependency_injector import containers, providers



from .service.health import HealthService
from .service.player_service import PlayerService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            "player_scoreboard_api"
        ]
    )

    application = providers.Dependency()

    health_service: HealthService = providers.Singleton(HealthService)
    player_service: PlayerService = providers.Singleton(PlayerService)
