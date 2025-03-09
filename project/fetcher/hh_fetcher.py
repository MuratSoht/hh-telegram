from datetime import datetime
from typing import Dict
from .base_hh_fetcher import BaseHhProccer
class HhFetcher(BaseHhProccer):
    def __init__(self, response_general_vacancy: Dict, response_detail_vacancy: Dict):
        self.response_general_vacancy = response_general_vacancy
        self.response_detail_vacancy = response_detail_vacancy

    def get_state(self):
        return {
            'id': self.get_id(),
            'title': self.get_title(),
            'salary': self.get_salary(),
            'url': self.get_url(),
            'work-format': self.get_work_format(),
            'published-date': self.get_published_date(),
            'city': self.get_city(),
            'experimence': self.get_experience(),
            'skills_keys': self.get_skills_keys(),
            'description': self.get_descriptions(),
        }
    
    def get_id(self):
        return self.response_general_vacancy.get('id')
    
    def get_title(self):
        return self.response_general_vacancy.get('name').replace('\xa0', ' ')
    
    def get_salary(self):
        salary = self.response_general_vacancy.get('salary')
        if salary:
            start_salary = salary.get('from')
            end_salary = salary.get('end')
            currency = salary.get('currency')
            if start_salary is None and end_salary is None:
                return None
            if start_salary is None:
                start_salary = '0'
            if end_salary is None:
                end_salary = start_salary
            return f'{start_salary}-{end_salary} {currency}'
        return None
    
    def get_url(self):
        return self.response_general_vacancy.get('alternate_url')
    
    def get_work_format(self):
        try:
            work_format = self.response_general_vacancy['work_format'][0]['name'].replace('\xa0', ' ')
            return work_format
        except IndexError:
            return 'Работа в офисе'

    def get_published_date(self):
        date = self.response_general_vacancy.get('published_at')
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    
    def get_city(self):
        try:
            return self.response_general_vacancy['area']['name']
        except KeyError:
            return None
        
    def get_experience(self):
        try:
            return self.response_general_vacancy['experience']['name']
        except:
            return None

    def get_skills_keys(self):
        skills_keys = self.response_detail_vacancy.get('key_skills')
        skills_keys_list = []
        if skills_keys:
            for skill in skills_keys:
                skills_keys_list.append(skill.get('name'))
            return skills_keys_list
        else:
            return None
    def get_descriptions(self):
        return self.response_detail_vacancy.get('description')

    def get_archive(self):
        return 