from parser import HeadHunterAPI, SuperJobAPI
from json_saver import HeadHunterSaver, SuperJobSaver

hh_data = HeadHunterAPI()
sj_data = SuperJobAPI()


def user_interaction():
    print('Доступные платформы для поиска:\n1. HeadHunter\n2. SuperJob')
    search_query = int(input('Выберите платформу: '))
    if search_query == int('1'):
        keyword = input('Введите ключевое слово для поиска на HeadHunter: ')
        json_saver = HeadHunterSaver('hh.json')
        vacancies = hh_data.post_data(keyword)
        json_saver.write_vacancies(vacancies)
        for vacancy in vacancies:
            print(vacancy)
            print('-' * 20)
            print('Количество найденных вакансий на Headhunter:', len(vacancies))
    elif search_query == int('2'):
        keyword = input('Введите ключевое слово для поиска на SuperJob: ')
        json_saver = SuperJobSaver('sj.json')
        vacancies = sj_data.post_data(keyword)
        json_saver.write_vacancies(vacancies)
        for vacancy in vacancies:
            print(vacancy)
            print('-' * 20)
            print('Количество найденных вакансий на SuperJob:', len(vacancies))
    else:
        print('выберите из предложенных двух')


print(user_interaction())