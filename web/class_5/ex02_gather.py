import asyncio
from time import time


async def sub_function():
    await asyncio.sleep(2)
    # print("Hello from sub function")
    return "Hello from sub function"


async def main():
    result = []
    print("Hello from asyncio")
    result = await asyncio.gather(sub_function(), sub_function())
    print(f"coro {result = }")
    return result
    

if __name__ == "__main__":
    start_time = time()
    result = asyncio.run(main())
    end_time = time() - start_time
    print(f"Entry point {result = }, {end_time = }")