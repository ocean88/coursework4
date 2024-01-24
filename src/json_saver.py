import json
from vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename):
        self.filename = filename
        self.vacancies = []

    def write_vacancies(self, vacancies):
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def read_vacancies(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            vacancies = json.load(file)
            list_vacancies = []
            for vacancy in vacancies:
                list_vacancies.append(Vacancy(vacancy['name'], vacancy['url'],
                                              vacancy['payment_from'],
                                              vacancy['payment_to']))

            return list_vacancies

