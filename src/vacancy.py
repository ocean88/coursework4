from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class HHVacancy(AbstractVacancy):
    def __init__(self, title, url, salary_from, salary_to):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f"""Название: {self.title}\nСсылка: {self.url}\nЗарплата от: {self.salary_from} до: {self.salary_to}"""

    def __lt__(self, other):
        return self.salary_from < other.salary_from


class SuperJobVacancy(AbstractVacancy):
    def __init__(self, title, url, payment_from, payment_to):
        self.title = title
        self.url = url
        self.payment_from = payment_from
        self.payment_to = payment_to

    def __str__(self):
        return f"""Название: {self.title}\nСсылка: {self.url}\nЗарплата от: {self.payment_from} до: {self.payment_to}"""

    def __lt__(self, other):
        return self.payment_from < other.payment_from