from typing import Callable
from trio import open_nursery, run, to_thread
from ws import ChatClient

async def text_input():
    return await to_thread.run_sync(input)

async def send_loop(send_fn: Callable):
    while True:
        await send_fn(await text_input())

async def main():
    async with open_nursery() as nursery:
        ws = ChatClient("ws://localhost:6969", print, nursery)
        nursery.start_soon(send_loop, ws.send)

run(main)