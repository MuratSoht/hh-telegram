from datetime import datetime
from typing import Dict
class HhFetcherVacansyList():
    def __init__(self, response: Dict):
        self.response = response

    def get_id(self):
        return self.response.get('id')
    
    def get_title(self):
        return self.response.get('name')
    
    def get_salary(self):
        salary = self.response.get('salary')
        if salary:
            start_salary = salary.get('from')
            end_salary = salary.get('end')
            currency = salary.get('currency')
            price = ''
            if start_salary is None and end_salary is None:
                return None
            if start_salary is None:
                start_salary = '0'
            if end_salary is None:
                end_salary = start_salary
            return f'{start_salary}-{end_salary} {currency}'
        return None
    def get_url(self):
        return self.response.get('alternate_url')
    
    def get_work_format(self):
        try:
            work_format = self.response['work_format'][0]['name'].replace('\xa0', ' ')
            return work_format
        except IndexError:
            return 'Работа в офисе'

    def get_published_date(self):
        date = self.response.get('published_at')
        date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')
        formatted_date = date_obj.strftime('%Y-%m-%d')
        return formatted_date
    
    def get_city(self):
        try:
            return self.response['area']['name']
        except KeyError:
            return None
    def get_experience(self):
        try:
            return self.response['experience']['name']
        except:
            return None

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
        }

class HhFetcherVacancyDetails():
    def __init__(self, response):
        self.response = response

    def get_skills_keys(self):
        skills_keys = self.response.get('key_skills')
        skills_keys_list = []
        if skills_keys:
            for skill in skills_keys:
                skills_keys_list.append(skill.get('name'))
            return skills_keys_list
        else:
            return None
    def get_descriptions(self):
        return self.response.get('description')

    def get_state(self):
        return {
            'skills_keys': self.get_skills_keys(),
            'description': self.get_descriptions(),
        }