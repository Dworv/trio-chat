from trio import open_nursery, sleep, run, to_thread
# from trio_websocket import open_websocket_url


async def text_input(prompt):
    return await to_thread.run_sync(input, prompt)

async def loop1():
    i = 1
    while i:
        i+=1
        print("Loop", i)
        await sleep(5)

async def loop2():
    while True:
        res = await text_input("What's up?\n")
        print("You said", res)

async def main():
    async with open_nursery() as nursery:
        nursery.start_soon(loop1)
        nursery.start_soon(loop2)


run(main)