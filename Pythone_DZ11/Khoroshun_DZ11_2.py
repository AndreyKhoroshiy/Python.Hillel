import requests
# import json
import csv


url = "https://api.forismatic.com/api/1.0/"


def response(url):
    get_res = requests.get(url, params=dict(method='getQuote', lang='ru', format='json'))
    return get_res


get_response = response(url)
# print(get_response.json())


i = 0
collection_of_quote = []
while i <= 19:
    get_response = response(url)
    if (get_response.json()['quoteAuthor'] != '') and (get_response.json() not in collection_of_quote):
        collection_of_quote.append(get_response.json())
        i += 1
print(collection_of_quote)
print(len(collection_of_quote))


def sort_name_author(tmp_dict):
    name = tmp_dict['quoteAuthor'].strip().split(" ")[-1]
    print(name)
    return name


sort_collection_of_quote = []
for item in collection_of_quote:
    generate_dict = {i: item[i] for i in item if (i != 'senderName') and (i != 'senderLink')}
    sort_collection_of_quote.append(generate_dict)


sort_collection_of_quotes = sorted(sort_collection_of_quote, key=sort_name_author)
print(sort_collection_of_quotes)


final_quote_list = []
for i in sort_collection_of_quote:
    i['Цитата'] = i.pop('quoteText')
    i['Автор'] = i.pop('quoteAuthor')
    i['Ссылка'] = i.pop('quoteLink')
    i = {'Автор': i['Автор'], 'Цитата': i['Цитата'], 'Ссылка': i['Ссылка']}
    final_quote_list.append(i)
print(final_quote_list)


def write_csv(data, filename_with_path):
    names = list(data[0].keys())
    with open(filename_with_path, 'wb') as output_file:
        csv_writer = csv.DictWriter(output_file, names)
        csv_writer.writeheader()
        csv_writer.writerows(data)


csv_writers = write_csv(final_quote_list, 'quotes.csv')

