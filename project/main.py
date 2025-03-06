from config import QUERIES
from async_fetch import AsyncFetcher
import asyncio
import aiohttp
import time

async def main():
    async with aiohttp.ClientSession() as session:
        async_fetcher = AsyncFetcher()
        vacancyis_list_task = []
        for query in QUERIES:
            params = {
                "text": query,
                "per_page": 100
            }
            vacancyis_list_task.append(asyncio.create_task(async_fetcher.fetch_vacancies(session, params)))
        res = await asyncio.gather(*vacancyis_list_task)
        cnt = 0
        res_list = []
        id_list = []
        for i in res:
            for j in i:
                cnt+=1
                id_list.append(j['id'])
                vacancy_task = asyncio.create_task(async_fetcher.fetch_vacancy(session, j['id']))
                vacancy = await vacancy_task
                merged_dict = {**j, **vacancy}

        # print(res_list)
        print(id_list)
        print(cnt)
if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)

