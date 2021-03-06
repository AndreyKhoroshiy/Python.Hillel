import random
import string
import json
import csv


def generate_string():
    my_list = []
    my_str = (''.join(random.choice(string.digits + random.choice(
        [' ', '.', ',', ':', ';', '-', '""', '/', '?', '!', '_', ' ']) + string.ascii_letters) for _ in range(91)))
    for i in range(9):
        my_str1 = (''.join(random.choice(string.ascii_letters + string.digits + random.choice([' ', '.', ',', ':', ';',
                                                                                               '-', '""', '/' '?', '!',
                                                                                               '_', ' '])) for _ in
                           range(100)))
        my_list.append(my_str1 + '\n')
    my_list.append(my_str)
    new_str = ''.join(my_list)
    print(new_str)
    print(len(new_str))
    return new_str


def my_dict():
    list_key = [(''.join(random.choice(string.ascii_lowercase) for _ in range(5))) for _ in
                range(random.randrange(5, 21))]
    list_value = random.choices([random.randrange(-100, 101), random.uniform(0, 1), True, False], k=len(list_key))
    my_new_dict = dict((key, value) for key, value in zip(list_key, list_value))
    print(my_new_dict)
    return my_new_dict


def table():
    n = random.randrange(3, 11)
    m = random.randrange(3, 11)
    my_table = [[random.choice([0, 1]) for _ in range(m)] for _ in range(n)]
    print(my_table)
    return my_table


def write_txt(data, filename_with_path='data.txt'):
    with open(filename_with_path, 'w') as txt_file:
        txt_file.write(data)


def write_json(data, filename_with_path='data.json'):
    with open(filename_with_path, 'w') as json_file:
        json.dump(data, json_file)


def write_csv(data, filename_with_path='data.csv'):
    with open(filename_with_path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
        csv_writer.writerows(data)


def file_writer(filename_with_path):
    mode = filename_with_path.rsplit('.')[-1]
    if mode == 'txt':
        write_txt(generate_string(), filename_with_path)
    elif mode == 'json':
        write_json(my_dict(), filename_with_path)
    elif mode == 'csv':
        write_csv(table(), filename_with_path)
    else:
        raise Exception('Unsupported file format!')


file_writer('.txt')
