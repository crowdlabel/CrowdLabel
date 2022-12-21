import pytest
from httpx import AsyncClient
from pathlib import Path

import aiohttp

from main import app
from test_main import req1, resp1, __register, __credits, __login


import asyncio

__register(req1)
__register(resp1)

t1 = __login(req1)
t2 = __login(resp1)

__credits(t1, 1e6)
__credits(t2, 1e6)

example_task = Path('D:/example_task.zip')

f = open(example_task, 'rb')
files = {'task_file': f}

async def test_upload(session):
    with open(example_task, 'rb') as f:
        async with session.post('http://localhost:8000/tasks/upload',
            headers=t1,
            data={'tasks_file': f},
        ) as response:

            print(response.status)

async def main():
    async with aiohttp.ClientSession() as session:
        coros = [test_upload(session) for _ in range(100)]
        await asyncio.gather(*(coros))


if __name__ == '__main__':
    #asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy)
    asyncio.run(main())
    