from typing import Callable
from trio import Nursery
from trio_websocket import serve_websocket, WebSocketConnection

class ChatServer:
    def __init__(self, url: str, port: int, serve: Callable):
        self.url = url
        self.port = port
        self.serve = serve
    
    async def start(self):
        self.conn: WebSocketConnection = await serve_websocket(self.serve, self.url, self.port, None)
    
    async def send(self, msg: str):
        await self.conn.send_message(msg)
    
    async def receive(self):
        return await self.conn.get_message()