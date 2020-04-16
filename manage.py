import os
from dotenv import load_dotenv
from scripts import get_superjob_vacancies, get_superjob_language_statistic
from scripts import get_hh_vacancies, get_hh_language_statistic
from scripts import print_languages_statistic


def get_superjob_languages_statistic(languages):
   
    languages_statistic = []

    for language in languages:

        all_language_vacancies = get_superjob_vacancies(superjob_secret_key, language, SYPERJOB_TOWN_ID, SYPERJOB_INDUSTRY_KEY, PERIOD)
        vacancies_found, vacancies_processed, vacancies_average_salary = get_superjob_language_statistic(all_language_vacancies)

        languages_statistic.append({
            'language_title': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': vacancies_average_salary
            })

    return languages_statistic


def get_hh_languages_statistic(languages):
   
    languages_statistic = []

    for language in languages:

        all_language_vacancies = get_hh_vacancies(language, HEADHUNTER_TOWN_ID, PERIOD)
        vacancies_found, vacancies_processed, vacancies_average_salary = get_hh_language_statistic(all_language_vacancies)

        languages_statistic.append({
            'language_title': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'average_salary': vacancies_average_salary
            })

    return languages_statistic


if __name__ == "__main__":

    HEADHUNTER_TOWN_ID = 1
    SYPERJOB_TOWN_ID = 4
    SYPERJOB_INDUSTRY_KEY = 48
    PERIOD = 30

    load_dotenv()
    superjob_secret_key=os.getenv("SYPERJOB_SECRET_KEY")

    superjob_table_title = 'SuperJob Moscow'
    hh_table_title = 'HeadHunter Moscow'

    languages = ['python', 'java', 'javascript', 'ruby', 'php', 'c++', 'c#','go', 'shell', 'typescript']

    superjob_languages_statistic = get_superjob_languages_statistic(languages)
    print_languages_statistic(superjob_languages_statistic, superjob_table_title)

    hh_languages_statistic = get_hh_languages_statistic(languages)
    print_languages_statistic(hh_languages_statistic, hh_table_title)