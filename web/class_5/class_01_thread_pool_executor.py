import asyncio
import concurrent.futures
from time import time


def blocks(n):
    counter = n
    start = time()
    while counter > 0:
        counter -= 1
    return f'{n=}: {time() - start}'


async def monitoring():
    while True:
        await asyncio.sleep(1)
        print(f'Monitoring {time()}')


async def run_blocking_tasks(executor, n):
    loop = asyncio.get_event_loop()
    print(f'{n=}: waiting for executor tasks')
    return await loop.run_in_executor(executor, blocks, n)


async def main():
    asyncio.create_task(monitoring())
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [run_blocking_tasks(executor, n) for n in [50_000_000, 60_000_000, 350_000_000]]
        return await asyncio.gather(*futures)


if __name__ == '__main__':
    result = asyncio.run(main())
    for r in result:
        print(r)
