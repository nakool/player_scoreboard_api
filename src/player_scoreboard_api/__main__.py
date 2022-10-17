import asyncio
import uvicorn

from .application import Application


async def main():
    _config = uvicorn.Config(
        app=Application(),
        host="0.0.0.0",
        port=8080
    )
    _server = uvicorn.Server(_config)
    await _server.serve()


if __name__ == "__main__":
    asyncio.run(main())
