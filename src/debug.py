from abc import ABC, abstractmethod
import requests


class AbstractAPI(ABC):
    @abstractmethod
    def get_data(self, search_query):
        pass

    @abstractmethod
    def post_data(self, search_query):
        pass


class HeadHunterAPI(AbstractAPI):
    def __init__(self):
        self.base_url = "https://api.hh.ru"

    def get_data(self, search_query):
        headers = {
            'authorization_code': 'I8RQ180OFUHFFE514PFETTJRDTV0RNMIQ7SCOHUNBPH5DGQ2U8FMMAFASQ6N7K6G'
        }
        params = {
            'text': {'keywords': search_query},
        }
        vacancies = requests.get('https://api.hh.ru/vacancies', headers=headers, params=params).json()

        return vacancies['items']

    def post_data(self, search_query):
        vacancies = self.get_data(search_query)
        vacancies_filtered = []
        for vacancy in vacancies:
            if not vacancy.get('salary'):
                salary_from = None
                salary_to = None
            else:
                salary_from = vacancy['salary']['from']
                salary_to = vacancy['salary']['to']
            vacancies_filtered.append(
                {
                    'name': vacancy['name'],
                    'url': vacancy['alternate_url'],
                    'salary_from': salary_from,
                    'salary_to': salary_to,
                }
            )
        return vacancies_filtered


hh = HeadHunterAPI()

print(hh.post_data('python'))