

class Vacancy:
    def __init__(self, title, url,salary_from, salary_to):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f"""Название: {self.title}\n
        Ссылка: {self.link}
"""