
from aiohttp.web_response import json_response


async def ping(request):
    return json_response({"msg": "pong"})
