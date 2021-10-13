import asyncio
import os
from asyncio import Task, BaseEventLoop, events
from threading import Thread
from time import time, sleep
import aiohttp

def write_image(data: bytes):
    filename: str = f'file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url: str, session: aiohttp.ClientSession):
    # async with session.get(url=url, allow_redirects=True) as response:
    #     data = await response.read()
    #     write_image(data=data)


    def test():
        sleep(1)
        print('executed')
        #asyncio.sleep()
        return 'uuuuuuuuuu'




    #await asyncio.create_task(test())

    #loop = events.get_running_loop()
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, test)
    #asyncio.wait([test() for _ in range(1)])

    #await asyncio.sleep(1)
    #await test()
    return result[0]


async def main2():
    url: str = 'https://loremflicker.com/320/240'
    tasks : [asyncio.tasks] = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url=url, session=session))
            tasks.append(task)

        await asyncio.gather(*tasks)



if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)