import requests


def predict_salary(salary_from, salary_to):
    predict_salary = (salary_from + salary_to)/2
    return predict_salary


def predict_rub_salary_for_hh(vacancy):

    salary = vacancy['salary']

    if salary is None:
        return None

    currency = vacancy['salary']['currency']
    salary_from = vacancy['salary']['from']
    salary_to = vacancy['salary']['to']

    if currency!='RUR':
        return None

    if salary_from is None and salary_to is not None:
        average_salary = salary_to*0.8
        return average_salary

    if salary_from is not None and salary_to is None:
        average_salary = salary_from*1.2
        return average_salary

    average_salary = predict_salary(salary_from, salary_to)

    return average_salary
    

def get_hh_vacancies(language, town, period):
    
    url = 'https://api.hh.ru/vacancies'

    page = 0
    pages_number = 1
    language_all_vacancies = []
    vacancy_text = f'программист {language}'

    while page < pages_number:

        params = {
            'text': vacancy_text, 
            'area': town, 
            'period': period,
            'page': page
            }
        response = requests.get(url, params=params)
        response.raise_for_status()
        page_vacancies = response.json()['items']
        language_all_vacancies.extend(page_vacancies)

        pages_number = response.json()['pages']
        page += 1

    return language_all_vacancies


def language_average_salary(vacancies_average_salary, vacancies_processed):
    try:
        vacancies_average_salary = int(sum(vacancies_average_salary)/vacancies_processed)
    except ZeroDivisionError:
        vacancies_average_salary = 0
    return vacancies_average_salary


def get_hh_language_statistic(vacancies):
    average_salaries = []
    for vacancy in vacancies:
        average_salary = predict_rub_salary_for_hh(vacancy)
        if average_salary is None:
            continue
        average_salaries.append(average_salary)
    
    vacancies_found = len(vacancies)
    vacancies_processed = len(average_salaries)
    vacancies_average_salary = language_average_salary(average_salaries, vacancies_processed)

    return vacancies_found, vacancies_processed, vacancies_average_salary