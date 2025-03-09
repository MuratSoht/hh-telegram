from abc import ABC
from aiohttp import ClientSession
from typing import Dict
class BaseAsyncClient(ABC):
    async def get_list_vacancies(self, session: ClientSession, params: Dict):
        pass

    async def get_vacancy(self, session: ClientSession, vacancy_id: str):
        pass
