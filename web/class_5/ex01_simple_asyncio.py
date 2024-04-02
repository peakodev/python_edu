import asyncio
from time import time


async def sub_function():
    await asyncio.sleep(2)
    # print("Hello from sub function")
    return "Hello from sub function"


async def main():
    result = []
    coro1 = sub_function()
    coro2 = sub_function()
    print("Hello from asyncio")
    result1 = await coro1
    result2 = await coro2
    result.append(result1)
    result.append(result2)
    print(f"coro {result = }")
    return result


if __name__ == "__main__":
    start_time = time()
    result = asyncio.run(main())
    end_time = start_time - time()
    print(f"Entry point {result = }, {end_time = }")
