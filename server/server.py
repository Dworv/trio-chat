from trio import open_nursery, run
from trio_websocket import WebSocketRequest, WebSocketConnection, ConnectionClosed
from ws import ChatServer

clients: dict[str, WebSocketConnection] = {}

async def serve(request: WebSocketRequest):
    client: WebSocketConnection = await request.accept()
    name = await client.get_message()
    clients[name] = client
    while True:
        try:
            res = await client.get_message()
            print("A client said:", res)
            for user in clients:
                if user is not name:
                    await clients[user].send_message(f"{name}: {res}")
        except ConnectionClosed:
            print("Client Disconnected")

async def main():
    await ChatServer("localhost", 6969, serve).start()
    

run(main)