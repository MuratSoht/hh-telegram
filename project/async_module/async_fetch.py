from aiohttp import ClientSession
from config import HH_API_URL
from typing import Dict, Any
from fetcher.hh_fetcher import HhFetcher
from .base_async_client import BaseAsyncClient
import asyncio
import time


class AsyncFetcher(BaseAsyncClient):
    def __init__(self):
        self.base_url = HH_API_URL

    async def get_list_vacancies(self, session: ClientSession, params: Dict):
        async with session.get(self.base_url + 'vacancies', params=params) as response:
            vacancy_list_json = await response.json()
            vacancy_list_json = vacancy_list_json.get('items', [])
            return vacancy_list_json
        
    async def get_vacancy(self, session: ClientSession, vacancy_id: str):
        vacancy = {}
        while vacancy.get('description') is None:
            async with session.get(self.base_url + 'vacancies/' + vacancy_id) as response:
                vacancy = await response.json()
                if vacancy.get('description') is not None:
                    return vacancy