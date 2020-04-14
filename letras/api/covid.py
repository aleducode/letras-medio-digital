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
total_cases = covid['latest_stat_by_country'][0]['total_cases']
active_cases = covid['latest_stat_by_country'][0]['active_cases']
last_update =  covid['latest_stat_by_country'][0]['record_date']
