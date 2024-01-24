from parser import HeadHunterAPI, SuperJobAPI
from json_saver import JSONSaver


if __name__ == '__main__':

    data = SuperJobAPI()
    json_saver = JSONSaver('superjob.json')
    vacancies = data.post_data('python')
    json_saver.write_vacancies(vacancies)
    list_vacancies_result = json_saver.read_vacancies()
    for vacancy in vacancies:
        print(vacancy)
        print('-' * 20)
