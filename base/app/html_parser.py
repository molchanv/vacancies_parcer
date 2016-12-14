import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    r = urllib.request.urlopen(url)
    return r.read()

# HTML PARSER for HEAD HUNTER

def sector_hh(html):
    # В список будут записаны отрасли компании
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