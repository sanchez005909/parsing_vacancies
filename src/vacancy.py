from abc import ABC, abstractmethod
import re


class Vacancy(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_list_vacancies(self):
        pass

    @abstractmethod
    def get_salary(self, vacancy):
        pass


class VacancyHH(Vacancy, ABC):

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def get_list_vacancies(self):
        vacancies = []
        for vacancy in self.vacancies_list:
            salary_currency, salary_from, salary_to = self.get_salary(vacancy)
            vacancy_dict = {'Должность': vacancy["name"],
                            'Местоположение': vacancy["area"]["name"],
                            'Зарплата': {'от': salary_from, 'до': salary_to, 'валюта': salary_currency},
                            'Описание': vacancy['snippet']['requirement'],
                            'Ссылка на вакансию': vacancy["alternate_url"],
                            }
            vacancies.append(vacancy_dict)
        return vacancies

    def get_salary(self, vacancy):
        if vacancy['salary'] is None:
            salary_from, salary_to, salary_currency = 0, 'не указано', 'RUR'
            return salary_currency, salary_from, salary_to
        salary_currency = vacancy['salary']['currency']
        salary_from = vacancy['salary']['from']
        salary_to = vacancy['salary']['to']
        if salary_currency is None:
            salary_currency = 'RUR'
        if salary_from is None:
            salary_from = 0
        elif salary_to is None:
            salary_to = 'не указано'
        return salary_currency, salary_from, salary_to


class VacancySuperJob(Vacancy, ABC):

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def get_list_vacancies(self):
        vacancies = []
        for vacancy in self.vacancies_list:
            salary_currency, salary_from, salary_to = self.get_salary(vacancy)
            print(vacancy['candidat'])
            description = self.validation_data(vacancy['candidat'])
            print(description)
            vacancy_dict = {'Должность': vacancy["profession"],
                            'Местоположение': vacancy["address"],
                            'Зарплата': {'от': salary_from, 'до': salary_to, 'валюта': salary_currency},
                            'Описание': vacancy['candidat'],
                            'Ссылка на вакансию': vacancy["link"],
                            }
            vacancies.append(vacancy_dict)
        return vacancies

    @staticmethod
    def validation_data(data):
        res = re.sub(r'[^\w\s\\. ]', '', data)
        return res

    def get_salary(self, vacancy):
        # print(vacancy, '\n')
        salary_from = vacancy['payment_from']
        salary_to = vacancy['payment_to']
        salary_currency = vacancy['currency']
        return salary_currency, salary_from, salary_to
