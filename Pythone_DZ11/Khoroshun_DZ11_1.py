import json


def reading_file():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        # print(data, type(data))
    return data


def sort_name(tmp_dict):
    name = tmp_dict.get('name')
    return name.split()[-1]


def sort_death(tmp_dict):
    years = tmp_dict.get('years')
    years = str(years)
    years = years.replace("c.", "")
    years = years.replace(".", "")
    years = years.strip()
    if len(years) > 12:
        years = years.replace("BC", "")
        years = years.strip()
        years = years[6:10]
        years = years.replace(" ", "-")
    if len(years) > 4:
        years = years[6:12]
        years = years.strip()
    years = int(years)
    # print(years, type(years))
    return years


def sort_text(tmp_dict):
    text = tmp_dict.get('text')
    return len(text.split(" "))


read_data = reading_file()
sorted_death = reading_file()
sorts_text = reading_file()

sorted_name_list = sorted(read_data, key=sort_name)
sorted_death_list = sorted(sorted_death, key=sort_death)
sorted_text_list = sorted(sorts_text, key=sort_text)
print(sorted_name_list)
print(sorted_death_list)
print(sorted_text_list)
