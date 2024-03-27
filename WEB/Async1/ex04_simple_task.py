from async_util import async_timeit, async_timeit1
from faker import Faker
import asyncio
from pprint import pprint as print


fake = Faker()

@async_timeit1
async def get_user_async(uid: int) -> dict:
    await asyncio.sleep(0.5)
    return {'id': uid, 'name': fake.name(), 'company': fake.company(), 'email': fake.email()}

@async_timeit1
async def main():
    tasks = []
    for i in range(6):
        tasks.append(asyncio.create_task(get_user_async(i)))
    print(tasks)
    result = []
    for task in tasks:
        result.append(await task)
    return result


if __name__ == '__main__':
    #result = asyncio.run(get_user_async(1))
    result = asyncio.run(main())
    print(result)