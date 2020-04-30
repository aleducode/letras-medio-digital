import requests
from bs4 import BeautifulSoup

url = "https://corona.help/country/colombia"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#Total casos
def total_cases():
    Tc = soup.select('h2')[1].text
    return Tc

def total_deaths():
    Td = soup.find_all('h2', class_='text-bold-700 danger')[0].text
    return Td

def total_recovered():
    Tr = soup.find_all('h2', class_='text-bold-700 success')[0].text
    return Tr

def active_cases():
    Ac = soup.find_all('h2', class_='text-bold-700 info')[0].text
    return Ac





