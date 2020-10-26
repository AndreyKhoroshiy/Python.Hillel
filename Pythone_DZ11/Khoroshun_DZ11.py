import json
from operator import itemgetter


def reading_file():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


read_data = reading_file()
reading_file()


def sort_name():
    data_name = sorted(read_data, key=itemgetter('name'))
    print(data_name)
    return data_name


data_sort_name = sort_name()
sort_name()


