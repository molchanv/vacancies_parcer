import requests
from base.app.html_parser import sector_hh, get_html
from base.forms import EmployerForm
from base.models import Employer

user_agent = {'User-agent': 'api-test-agent'}

def to_db(employers):
    for employer in employers:
        url = 'https://api.hh.ru/employers/%s' % (employer)
        normal_url = 'https://hh.ru/employer/%s' % (employer)
        r = requests.get(url, headers=user_agent)
        employer = r.json()
        count = get_vacancy_count(employer['vacancies_url'])
        address = get_address(url)
        sector = get_sector(normal_url)
        employer_info = {
            'name': employer['name'],
            'link': employer['site_url'],
            'vacancy_count': count,
            'address': address,
            'sector': ','.join(sector)
        }
        try:
            obj = Employer.objects.get(name=employer['name'])
        except Employer.DoesNotExist:
            new_employer = EmployerForm(employer_info)
            if new_employer.is_valid():
                new_employer.save()


# HEAD HUNTER API

# Получить первые 2000 вакансий по России с текстом "Продавец консультант"
def hh_parser():
    # В список записываются id работодателей
    employers = []
    # Страница с которой начинается сбор информации (max - 99)
    page = 90
    while page != 100:
        url = 'https://api.hh.ru/vacancies?text=Продавец+консультант&area=113&order_by=publication_time&page=%s' % (page)
        r = requests.get(url, headers=user_agent)
        vacancies = r.json()['items']
        for vacancy in vacancies:
            employers.append(vacancy['employer']['id'])
        page += 1
    # Возвращает список без дубликатов id
    return set(employers)

def get_vacancy_count(vacancies_url):
    r = requests.get(vacancies_url, headers=user_agent)
    count = len(r.json()['items'])
    return count

def get_address(employer_url):
    r = requests.get(employer_url, headers=user_agent)
    address = r.json()['area']['name']
    return address

# получить отрасли компании по её ссылке
def get_sector(employer_url):
    return sector_hh(get_html(employer_url))

