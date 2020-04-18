import requests
import json
url = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/latest_stat_by_country.php"

querystring = {"country":"Colombia"}

headers = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "d0d716a88cmshade9c0371aa413dp15f9bdjsnc7ec971ecf32"
    }


response = requests.request("GET", url, headers=headers, params=querystring)

def get_info():
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None
covid = get_info()
#print(covid)

def total_cases():
    total_cases = covid['latest_stat_by_country'][0]['total_cases']
    return total_cases

def active_cases():
    active_cases = covid['latest_stat_by_country'][0]['active_cases']
    return active_cases
def new_cases():
    new_cases = covid['latest_stat_by_country'][0]['new_cases']
    return new_cases

def total_deaths():
    total_deaths = covid['latest_stat_by_country'][0]['total_deaths']
    return total_deaths
def new_deaths():
    new_deaths = covid['latest_stat_by_country'][0]['new_deaths']
    return new_deaths

def total_recovered():
    total_recovered = covid['latest_stat_by_country'][0]['total_recovered']
    return total_recovered

def last_update():
    last_update =  covid['latest_stat_by_country'][0]['record_date']
    return last_update

