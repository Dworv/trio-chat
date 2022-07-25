from trio import open_nursery, sleep, run
from trio_websocket import open_websocket_url

URL = "localhost:6969"


async def connect(url: str):
    async with open_websocket_url(url) as conn:
        await conn.s


async def main():
    async with open_nursery() as nursery:
        nursery.start_soon(connect, URL)

