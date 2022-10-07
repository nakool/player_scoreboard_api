from dependency_injector import containers, providers

from .application import Application


class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            "player_scoreboard_api"
        ]
    )

    application: Application = providers.Dependency(instance_of=Application)
