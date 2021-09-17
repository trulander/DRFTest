import asyncio
from time import time
import aiohttp


def write_image(data: bytes):
    filename: str = f'file-{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url: str, session: aiohttp.ClientSession):
    async with session.get(url=url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data=data)


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