def get_filtering_data():
    """
    Работа с пользователем
    :return: 1) Поисковый запрос
    2) Нужна ли сортировка
    3) количество топ-вакансий
    """
    search_word = input('Введите поисковый запрос:')

    sorted_list = 0
    while int(sorted_list) not in (1, 2):
        sorted_list = input('Отсортировать список по ЗП? Введите:(1 - да, 2 - нет)')
        if sorted_list.isdigit():
            if int(sorted_list) not in (1, 2):
                print('Введено некорректное значение')
                print('Повторите попытку')
        else:
            sorted_list = 0
            print('Введено некорректное значение')
            print('Повторите попытку')

    while True:
        count_top_vacancies = input('Введите количество топ-вакансий для вывода (целое число)')
        if count_top_vacancies.isdigit():
            return search_word, sorted_list, count_top_vacancies
        else:
            print('Введено некорректное значение')
            print('Повторите попытку')
