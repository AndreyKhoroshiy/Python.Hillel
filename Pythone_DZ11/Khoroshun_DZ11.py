import json


def reading_file():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        # print(data, type(data))
    return data


def sort_name(mp_dict):
    name = mp_dict.get('name')
    return name.split()[-1]


read_data = reading_file()


sorted_name_list = sorted(read_data, key=sort_name)
print(sorted_name_list)

