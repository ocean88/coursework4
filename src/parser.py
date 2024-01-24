from abc import ABC, abstractmethod
import requests
from dotenv import load_dotenv
import os

load_dotenv()
hh_token = os.environ.get('HHKEY')
superjob_token = os.environ.get('SUPERJOBKEY')


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
            'authorization_code': hh_token
        }
        params = {
            'text': search_query
        }
        vacancies = requests.get('https://api.hh.ru/vacancies', headers=headers, params=params).json()

        return vacancies

    def post_data(self, search_query):
        vacancies = self.get_data(search_query)
        vacancies_filtered = []
        for vacancy in vacancies:
            vacancies_filtered.append(
                {
                    'name': vacancy['name'],
                    'url': vacancy['alternate_url'],
                    'salary_from': vacancy['salary']['from'],
                    'salary_to': vacancy['salary']['to']
                }
            )
        return vacancies_filtered


class SuperJobAPI(AbstractAPI):
    def get_data(self, search_query):
        headers = {
            'X-Api-App-Id': superjob_token
        }
        params = {
            'keyword': {'query': search_query},
        }
        vacancies = requests.get('https://api.superjob.ru/2.0/vacancies/', headers=headers, params=params).json()

        return vacancies['objects']

    def post_data(self, search_query):
        vacancies = self.get_data(search_query)
        vacancies_filtered = []
        for vacancy in vacancies:
            vacancies_filtered.append(
                {
                    'name': vacancy['profession'],
                    'url': vacancy['link'],
                    'payment_from': vacancy['payment_from'],
                    'payment_to': vacancy['payment_to']
                }
            )
        return vacancies_filtered
