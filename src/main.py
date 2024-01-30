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
        list_vacancies_hh = json_saver.read_vacancies()
        for vacancy in list_vacancies_hh:
            print(vacancy)
            print('-' * 50)
        ask_question = input('Отсортировать вакансии по возрастанию? (y/n) ')
        if ask_question == 'y':
            for vacancy in sorted(list_vacancies_hh):
                print(vacancy)
                print('-' * 50)
            question_2 = input('Отобразить топ 5 зарплат? (y/n) ')
            if question_2 == 'y':
                top_5_salaries = sorted(list_vacancies_hh, key=lambda vacancy: vacancy.salary_from, reverse=True)[:5]
                for vacancy in top_5_salaries:
                    print(vacancy)
                    print('-' * 50)
            else:
                exit('Программа завершена')
        else:
            exit('Программа завершена')
    elif search_query == int('2'):
        keyword = input('Введите ключевое слово для поиска на SuperJob: ')
        json_saver = SuperJobSaver('sj.json')
        vacancies = sj_data.post_data(keyword)
        json_saver.write_vacancies(vacancies)
        list_vacancies_sj = json_saver.read_vacancies()
        for vacancy in list_vacancies_sj:
            print(vacancy)
            print('-' * 50)
        ask_question = input('Отсортировать вакансии по возрастанию? (y/n) ')
        if ask_question == 'y':
            for vacancy in sorted(list_vacancies_sj):
                print(vacancy)
                print('-' * 50)
            question_2 = input('Отобразить топ 5 зарплат? (y/n) ')
            if question_2 == 'y':
                top_5_salaries = sorted(list_vacancies_sj, key=lambda vacancy: vacancy.payment_from, reverse=True)[:5]
                for vacancy in top_5_salaries:
                    print(vacancy)
                    print('-' * 50)
            else:
                exit('Программа завершена')
        else:
            exit('Программа завершена')
    else:
        print('выберите из предложенных двух')


user_interaction()