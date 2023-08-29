from working_api import WorkingAPIHH
from jsonsaver import JsonSaver
from vacancy import Vacancy
import pprint

# объект для работы с АПИ HeadHunter
obj = WorkingAPIHH('', 1, True)

# получить список всех вакансий(ограничение 2 000 вакансий)
vacancies = obj.get_vacancies()

# подготовка списка вакансий к записи в файл.json
obj_vacancy = Vacancy(vacancies)
vacancies = obj_vacancy.get_list_vacancies()

# объект класса JsonSaver
json_saver = JsonSaver(vacancies)

# сохранение списка вакансий в json - файл
json_saver.save_to_json()

# фильтр вакансий по поисковому запросу
search_word = input('Введите поисковый запрос:')
filter_vacancies = json_saver.filter_vacancies(search_word)
if type(filter_vacancies) is list:
    print(*filter_vacancies, sep='\n')
else:
    print(filter_vacancies)

# вывод отсортированного списка вакансий по ЗП (от)
print(*json_saver.sort_by_salary(), sep='\n')


