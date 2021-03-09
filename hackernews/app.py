import os

import aiohttp_cors
import aiopg.sa
from aiohttp import web
from usagelogger.aiohttp import HttpLoggerForAIOHTTP

from hackernews.routes import init_routes


def init_config(app: web.Application, argv=None) -> None:
    pass


async def init_database(app: web.Application) -> None:
    """
    This is signal for success creating connection with database
    """

    engine = await aiopg.sa.create_engine(
        os.environ.get("DATABASE_URL", "postgres://postgres:postgres@postgres/postgres")
    )
    app["db"] = engine


async def close_database(app: web.Application) -> None:
    """
    This is signal for success closing connection with database before shutdown
    """
    app["db"].close()
    await app["db"].wait_closed()


def init_app(argv=None) -> web.Application:
    app = web.Application(
        middlewares=[
            HttpLoggerForAIOHTTP(
                rules="include debug",
            )
        ]
    )
    cors = aiohttp_cors.setup(app)

    init_config(app, argv)
    init_routes(app, cors)
    app.on_startup.extend([init_database])
    app.on_cleanup.extend([close_database])
    return app


app = init_app()
