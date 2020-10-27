import json
from operator import itemgetter


def reading_file():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        print(data, type(data))
    return data


read_data = reading_file()
reading_file()


def sort_name():
    # data_name = sorted(read_data, key=itemgetter('name'))
    for index in read_data:
        elements = index.get('name')
        my_string = "".join(elements)
        name = my_string.split(" ")[-1]
        # print(name)
    return name


data_sort_name = sort_name()
sort_name()


sorted_name_list = sorted(read_data, key=sort_name())
print(sorted_name_list)
