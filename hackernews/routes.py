import pathlib

import aiohttp_cors

from hackernews.api.views import gqil_view, gql_view
from hackernews.views import ping

PROJECT_PATH = pathlib.Path(__file__).parent.parent


def init_routes(app, cors):
    app.router.add_route("*", "/graphiql", gqil_view, name="graphiql")
    app.router.add_route("*", "/ping", ping, name="ping")

    resource = cors.add(
        app.router.add_resource(""),
        {
            "*": aiohttp_cors.ResourceOptions(
                expose_headers="*",
                allow_headers="*",
                allow_credentials=True,
                allow_methods=["POST", "PUT", "GET"],
            ),
        },
    )
    resource.add_route("POST", gql_view)
    resource.add_route("PUT", gql_view)
    resource.add_route("GET", gql_view)
