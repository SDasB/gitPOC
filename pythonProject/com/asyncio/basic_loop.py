import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print("Started at:", asyncio.get_running_loop().time())
    await say_after(1, "Hello AsyncIO")
    await say_after(5, "AsyncIO is powerful")

    print("Finished at:", asyncio.get_running_loop().time())


asyncio.run(main())