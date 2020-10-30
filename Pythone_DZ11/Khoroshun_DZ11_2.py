import requests
import json
import csv

res = requests.get('https://api.forismatic.com/api/1.0/')
print(res.status_code)


url = "https://api.forismatic.com/api/1.0/"


def response(url):
    get_res = requests.get(url, parameters=dict(method='getQuote', lang='ru', format='json'))
    return get_res


get_response = response()
print(get_response)
