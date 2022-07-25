from typing import Callable
from trio import Nursery
from trio_websocket import open_websocket_url, WebSocketConnection

URL = "localhost:6969"

class ChatClient:
    def __init__(self, url: str, track: Callable, nursery: Nursery):
        self.url = url
        self.track = track
        nursery.start_soon(self.connect)

    async def receive(self) -> str:
        if self.conn.closed:
            await self.connect()
        else:
            return await self.conn.get_message()
    
    async def send(self, msg):
        if self.conn.closed:
            await self.connect()
        else:
            await self.conn.send_message(msg)

    async def connect(self):
        async with open_websocket_url(self.url) as self.conn:
            self.conn: WebSocketConnection

            while not self.conn.closed:
                self.track(await self.receive())
