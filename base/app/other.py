import requests
import urllib.request
from bs4 import BeautifulSoup
from base.forms import EmployerForm
from base.models import Employer

user_agent = {'User-agent': 'api-test-agent'}

def to_db(employers):
    for employer in employers:
        url = 'https://api.hh.ru/employers/%s' % (employer)
        normal_url = 'https://hh.ru/employer/%s' % (employer)
        r = requests.get(url, headers=user_agent)
        employer = r.json()
        count = vacancy_count(employer['vacancies_url'])
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


def vacancy_count(vacancies_url):
    r = requests.get(vacancies_url, headers=user_agent)
    count = len(r.json()['items'])
    return count


def get_address(employer_url):
    r = requests.get(employer_url, headers=user_agent)
    address = r.json()['area']['name']
    return address

# HEAD HUNTER API

def hh_parser():
    employers = []
    page = 0
    while page != 100:
        url = 'https://api.hh.ru/vacancies?text=Продавец+консультант&area=113&order_by=publication_time&page=%s' % (page)
        r = requests.get(url, headers=user_agent)
        vacancies = r.json()['items']
        for vacancy in vacancies:
            employers.append(vacancy['employer']['id'])
        page += 1
    return set(employers)

# HTML PARSER for HEAD HUNTER

def get_sector(employer_url):
    return parse(get_html(employer_url))

def get_html(url):
    r = urllib.request.urlopen(url)
    return r.read()

def parse(html):
    l = []
    soup = BeautifulSoup(html, "html.parser")
    try:
        sidebar = soup.find('div', class_='company-sidebar')
        company_header = sidebar.find_all('p', class_='company-header')[-1]
        if company_header == 'Сферы деятельности':
            while company_header != None:
                l.append(company_header.text)
                company_header = company_header.nextSibling
    except:
        pass

    return l[1:]