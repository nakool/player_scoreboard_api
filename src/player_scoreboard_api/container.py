from dependency_injector import containers, providers




class Container(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(
        packages=[
            "player_scoreboard_api"
        ]
    )

    application = providers.Dependency()
