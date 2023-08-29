class Vacancy:

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def get_list_vacancies(self):
        vacancies = []
        for vacancy in self.vacancies_list:
            salary_currency, salary_from, salary_to = self.get_salary(vacancy)
            vacancy_dict = {}
            vacancy_dict = {'Должность': vacancy["name"],
                               'Местоположение': vacancy["area"]["name"],
                               'Зарплата': {'от': salary_from, 'до': salary_to, 'валюта': salary_currency},
                               'Требование': vacancy['snippet']['requirement'],
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

    def __repr__(self):
        return self.vacancies_list
