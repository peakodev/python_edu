import asyncio
from pprint import pprint as print

from faker import Faker

from async_util import async_timeit

fake = Faker()


@async_timeit
async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}


@async_timeit
async def main():
    tasks = []
    for i in range(6):
        tasks.append(asyncio.create_task(get_user_async(i)))
    print(tasks)
    result = []
    for task in tasks:
        result.append(await task)
    # result.append(await tasks[2])
    
    return result


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)