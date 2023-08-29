from working_api import WorkingAPIHH, WorkingAPISuperJob
from jsonsaver import JsonSaver
from vacancy import VacancyHH, VacancySuperJob
from functions import get_filtering_data

platform = int(input('Введите номер платформы для поиска(1 - HeadHunter, 2 - SuperJob): '))
if platform == 1:
    # объект для работы с АПИ HeadHunter
    obj = WorkingAPIHH()

    # получить список всех вакансий(ограничение 2 000 вакансий)
    vacancies = obj.get_vacancies()

    # подготовка списка вакансий к записи в файл.json
    obj_vacancy = VacancyHH(vacancies)
    vacancies = obj_vacancy.get_list_vacancies()

elif platform == 0:
    # объект для работы с АПИ SuperJob
    obj = WorkingAPISuperJob()
    # получить список всех вакансий(ограничение 500 вакансий)
    vacancies = obj.get_vacancies()
    # подготовка списка вакансий к записи в файл.json
    obj_vacancy = VacancySuperJob(vacancies)
    vacancies = obj_vacancy.get_list_vacancies()
else:
    quit('Выбранной платформы не существует')

# объект класса JsonSaver
json_saver = JsonSaver(vacancies)

# сохранение списка вакансий в json - файл
json_saver.save_to_json()

search_word, sorting, count_top = get_filtering_data()
if sorting == 2:
    # фильтр вакансий по поисковому запросу
    print(json_saver.filter_vacancies(search_word))
else:
    # фильтр вакансий по поисковому запросу
    filter_vacancies = json_saver.filter_vacancies(search_word)
    # вывод отсортированного списка вакансий по ЗП (от)
    sorting_vacancies = json_saver.sort_by_salary(filter_vacancies)
    print(f'Найдено {len(sorting_vacancies)} вакансий.')

    # вывод топ-вакансий
    if int(count_top) > len(sorting_vacancies):
        count_top = len(sorting_vacancies)
    print(f'Топ-{count_top} вакансий')
    top_vacancies = json_saver.get_top_vacancies(count_top, sorting_vacancies)
    print(*top_vacancies, sep='\n')
