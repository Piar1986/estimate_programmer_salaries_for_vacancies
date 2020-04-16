import requests


def predict_salary(salary_from, salary_to):
    predict_salary = (salary_from + salary_to)/2
    return predict_salary

def predict_rub_salary_for_SuperJob(vacancy):

    currency = vacancy['currency']
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']

    if currency!='rub':
        return None

    if salary_from == 0 and salary_to == 0:
        return None

    if salary_from == 0 and salary_to > 0:
        average_salary = salary_to*0.8
        return average_salary

    if salary_from > 0 and salary_to == 0:
        average_salary = salary_from*1.2
        return average_salary

    average_salary = predict_salary(salary_from, salary_to)
    
    return average_salary


def get_superjob_vacancies(secret_key, language, town_id, catalog_industry_key, period):
    
    url='https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id':secret_key}

    page = 0
    pages_number = 1
    language_all_vacancies = []

    while page < pages_number:

        params = {
            'keyword': language, 
            'town': town_id,
            'catalogues': catalog_industry_key,
            'period': period,
            'page': page
        }
        response = requests.get(url, headers=header, params=params)
        response.raise_for_status()
        page_vacancies = response.json()['objects']
        language_all_vacancies.extend(page_vacancies)

        pages_number = response.json()['total']
        page += 1

    return language_all_vacancies


def language_average_salary(vacancies_average_salary, vacancies_processed):
    try:
        vacancies_average_salary = int(sum(vacancies_average_salary)/vacancies_processed)
    except ZeroDivisionError:
        vacancies_average_salary = 0
    return vacancies_average_salary


def get_superjob_language_statistic(vacancies):
    average_salaries = []
    for vacancy in vacancies:
        average_salary = predict_rub_salary_for_SuperJob(vacancy)
        if average_salary is None:
            continue
        average_salaries.append(average_salary)
    
    vacancies_found = len(vacancies)
    vacancies_processed = len(average_salaries)
    vacancies_average_salary = language_average_salary(average_salaries, vacancies_processed)

    return vacancies_found, vacancies_processed, vacancies_average_salary