import requests
import json
import csv


url = "https://api.forismatic.com/api/1.0/"


def response(url):
    get_res = requests.get(url, params=dict(method='getQuote', lang='ru', format='json'))
    return get_res


get_response = response(url)
print(get_response.json())
