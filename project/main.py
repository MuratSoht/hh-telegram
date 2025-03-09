from config import PARAMS
from async_module.async_fetch import AsyncFetcher
from fetcher.hh_fetcher import HhFetcher
import asyncio
import aiohttp
import time

async def main():
    async with aiohttp.ClientSession() as session:
        async_fetcher = AsyncFetcher()
        vacancyis_list_task = []
        for params in PARAMS:
            vacancyis_list_task.append(asyncio.create_task(async_fetcher.get_list_vacancies(session, params)))
        res = await asyncio.gather(*vacancyis_list_task)
        cnt = 0
        for vacancy_query in res:
            for vacancy in vacancy_query:
                try:
                    task = asyncio.wait_for(asyncio.create_task(async_fetcher.get_vacancy(session, vacancy.get('id'))), timeout=100)
                    response_detail_vacancy = await task
                    ready_data = HhFetcher(vacancy, response_detail_vacancy).get_state()
                    print(ready_data)
                    print()
                    cnt+=1
                except asyncio.TimeoutError:
                    pass
        print(cnt)
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)

