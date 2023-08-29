from abc import ABC, abstractmethod
import requests


class WorkingAPI(ABC):

    @abstractmethod
    def get_vacancies(self, pages):
        pass


class WorkingAPIHH(WorkingAPI, ABC):

    def __init__(self, text='', period=10, only_with_salary=False):
        self.text = text
        self.period = period
        self.only_with_salary = only_with_salary

    def get_request(self, page=0):
        params = {'page': page,
                  'text': self.text,
                  'period': self.period,
                  'only_with_salary': self.only_with_salary,
                  'per_page': 100}
        response = requests.get('https://api.hh.ru/vacancies', params=params)
        if response.status_code == 200:
            return response
        return quit('Ошибка запроса!')

    def get_vacancies(self):
        result = self.get_request()
        pages = result.json()["pages"]
        vacancies = result.json()["items"]
        for page in range(1, pages):
            result = self.get_request(page).json()["items"]
            vacancies.extend(result)
        return vacancies


# class WorkingAPISuperjob(WorkingAPI):
#
#     def __init__(self, text='', period=10, only_with_salary=False):
#         self.text = text
#         self.period = period
#         self.only_with_salary = only_with_salary
#
#     def get_request(self):
#         pass

