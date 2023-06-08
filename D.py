import aiohttp
import asyncio
import time

async def make_request(session, url):
    async with session.get(url) as response:
        return await response.json()

async def measure_request_time():
    url = "http://httpbin.org/delay/3"
    num_requests = 100

    start_time = time.time()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(num_requests):
            task = asyncio.create_task(make_request(session, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)

    end_time = time.time()

    total_time = end_time - start_time
    print(f'Время работы функции: {total_time} секунд')

asyncio.run(measure_request_time())
