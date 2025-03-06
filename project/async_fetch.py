import aiohttp
from config import HH_API_URL
from typing import Dict, Any
from fetcher.hh_fetcher import HhFetcherVacansyList, HhFetcherVacancyDetails

class AsyncFetcher():
    def __init__(self):
        self.base_url = HH_API_URL

    async def fetch_vacancies(self, session: aiohttp.ClientSession, params: Dict[str, Any]):
        async with session.get(self.base_url + 'vacancies', params=params) as response:
            text = await response.json()
            text = text.get('items', [])
            res = []
            for i in text:
                res.append(HhFetcherVacansyList(i).get_state())
            return res
        
    async def fetch_vacancy(self, session: aiohttp.ClientSession, vacancy_id: int):
        async with session.get(self.base_url + 'vacancies/' + vacancy_id) as response:
            text = await response.json()
            return HhFetcherVacancyDetails(text).get_state()