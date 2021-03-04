import os

import aiohttp_cors
import aiopg.sa
from aiohttp import web

from hackernews.routes import init_routes
from hackernews.utils import get_config


def init_config(app: web.Application, argv=None) -> None:
    app["config"] = get_config(argv)


async def init_database(app: web.Application) -> None:
    """
    This is signal for success creating connection with database
    """
    config = app["config"]["postgres"]

    engine = await aiopg.sa.create_engine(**config)
    app["db"] = engine


async def close_database(app: web.Application) -> None:
    """
    This is signal for success closing connection with database before shutdown
    """
    app["db"].close()
    await app["db"].wait_closed()


def init_app(argv=None) -> web.Application:
    app = web.Application()
    cors = aiohttp_cors.setup(app)
    print(os.environ)
    init_config(app, argv)
    init_routes(app, cors)
    app.on_startup.extend([init_database])
    app.on_cleanup.extend([close_database])
    return app


app = init_app()
