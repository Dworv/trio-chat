from trio import open_nursery, run
from trio_websocket import WebSocketRequest, WebSocketConnection, ConnectionClosed
from ws import ChatServer

clients: list[WebSocketConnection] = []

async def serve(request: WebSocketRequest):
    client: WebSocketConnection = await request.accept()
    clients.append(client)
    while True:
        try:
            res = await client.get_message()
            print("A client said:", res)
            for _client in clients:
                if client is not _client:
                    await _client.send_message(res)
        except ConnectionClosed:
            print("Client Disconnected")

async def main():
    await ChatServer("localhost", 6969, serve).start()
    

run(main)