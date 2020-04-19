from terminaltables import AsciiTable

def print_languages_statistic(languages_statistic, table_title):

    table_data = [(
        'Язык', 
        'Вакансий найдено', 
        'Вакансий обработано', 
        'Средняя зарплата',
    )]

    for language in languages_statistic:

        language_title = language['language_title']
        vacancies_found = language['vacancies_found']
        vacancies_processed = language['vacancies_processed']
        average_salary = language['average_salary']

        row = (
            language_title, 
            vacancies_found, 
            vacancies_processed, 
            average_salary,
        )
        table_data.append(row)

    table = AsciiTable(table_data, table_title)
    print(table.table)