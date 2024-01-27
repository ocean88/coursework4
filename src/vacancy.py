from abc import ABC, abstractmethod


class AbstractVacancy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class HHVacancy(AbstractVacancy):
    def __init__(self, title, url, salary_from, salary_to):
        self.title = title
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to

    def __str__(self):
        return f"""Название: {self.title}\n
        Ссылка: {self.link}
    """

    def __eq__(self, other):
        return (isinstance(other, HHVacancy) and self.title == other.title
                and self.url == other.url and self.salary_from == other.salary_from
                and self.salary_to == other.salary_to)


class SuperJobVacancy(AbstractVacancy):
    def __init__(self, title, url, payment_from, payment_to):
        self.title = title
        self.url = url
        self.payment_from = payment_from
        self.payment_to = payment_to

    def __str__(self):
        return f"""Название: {self.title}\n
        Ссылка: {self.link}
    """

    def __eq__(self, other):
        return (isinstance(other, SuperJobVacancy) and self.title == other.title
                and self.url == other.url and self.payment_from == other.payment_from
                and self.payment_to == other.payment_to)