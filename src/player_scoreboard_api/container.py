from dependency_injector import containers, providers



from .service.health import HealthService

class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            "player_scoreboard_api"
        ]
    )

    application = providers.Dependency()

    health_service: HealthService = providers.Singleton(HealthService)
