import json


class JsonSaver:

    def __init__(self, vacancies_list):
        self.vacancies_list = vacancies_list

    def save_to_json(self):
        """
        сохранение списка вакансий в файл
        :return:
        """
        data = self.vacancies_list
        with open('vacancies.json', 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_vacancy(self, vacancy):
        """
        Добавить вакансию в файл
        :param vacancy: вакансия которую нужно добавить в файл
        :return: None
        """
        with open('vacancies.json', 'a') as file:
            json.dump(vacancy, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, *args):
        """
        Удаление вакансий
        :param args: номера вакансий которые нужно удалить
        :return: удаленные вакансии
        """
        with open('vacancies.json', 'r+', encoding='UTF-8') as file:
            vacancies = json.load(file)
            for i in args:
                if i-1 < len(vacancies):
                    vacancy = vacancies.pop(i)
                    print(f'Вакансия удалена: {vacancy}')
                else:
                    print(f'Невозможно удалить: номер {i} вакансии превышает количество вакансий.')
            json.dump(vacancy, file, ensure_ascii=False, indent=4)
            
    def sort_by_salary(self, filter_vacancies):
        """
        сортировка вакансий по ЗП
        :return: отсортированный список вакансий
        """
        vacancies_sorted = sorted(filter_vacancies, key=lambda x: int(x['Зарплата']['от']))
        return vacancies_sorted

    def filter_vacancies(self, search_word):
        filter_list = []
        for vacancy in self.vacancies_list:
            if search_word.lower() in vacancy["Должность"].lower():
                filter_list.append(vacancy)
        if not filter_list:
            return 'Вакансий не найдено'
        return filter_list

    def get_top_vacancies(self, num, sort_list):
        return sort_list[0: int(num)]

    def __repr__(self):
        return f'{self.vacancies_list}'
