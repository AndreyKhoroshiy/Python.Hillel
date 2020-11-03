import random
import string
import json
import csv


class FileWriter:

    def __init__(self, filename, file_data=None):
        self.filename = filename
        self.file_data = file_data if file_data is not None else self._data()

    def _generate_string(self):
        my_list = []
        my_str = (''.join(random.choice(string.digits + random.choice(
            [' ', '.', ',', ':', ';', '-', '""', '/', '?', '!', '_', ' ']) + string.ascii_letters) for _ in range(91)))
        for i in range(9):
            my_str1 = (
                ''.join(random.choice(string.ascii_letters + string.digits + random.choice([' ', '.', ',', ':', ';',
                                                                                            '-', '""', '/' '?', '!',
                                                                                            '_', ' '])) for _ in
                        range(100)))
            my_list.append(my_str1 + '\n')
        my_list.append(my_str)
        new_str = ''.join(my_list)
        # print(new_str)
        # print(len(new_str))
        return new_str

    def _my_dict(self):
        list_key = [(''.join(random.choice(string.ascii_lowercase) for _ in range(5))) for _ in
                    range(random.randrange(5, 21))]
        list_value = random.choices([random.randrange(-100, 101), random.uniform(0, 1), True, False], k=len(list_key))
        my_new_dict = dict((key, value) for key, value in zip(list_key, list_value))
        # print(my_new_dict)
        return my_new_dict

    def _table(self):
        n = random.randrange(3, 11)
        m = random.randrange(3, 11)
        my_table = [[random.choice([0, 1]) for _ in range(m)] for _ in range(n)]
        # print(my_table)
        return my_table

    def _data(self):
        mode = self.filename.rsplit('.')[-1]
        if mode == 'txt':
            self.file_data = self._generate_string()
        elif mode == 'json':
            self.file_data = self._my_dict()
        elif mode == 'csv':
            self.file_data = self._table()
        else:
            raise Exception('Unsupported file format!')
        return self.file_data

    def _write_txt(self):
        with open(self.filename, 'w') as txt_file:
            txt_file.write(self.file_data)

    def _write_json(self):
        with open(self.filename, 'w') as json_file:
            json.dump(self.file_data, json_file)

    def _write_csv(self):
        with open(self.filename, 'w') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=";", lineterminator='\n')
            csv_writer.writerows(self.file_data)

    def file_writer(self):
        mode = self.filename.rsplit('.')[-1]
        if mode == 'txt':
            data = self._write_txt()
        elif mode == 'json':
            data = self._write_json()
        elif mode == 'csv':
            data = self._write_csv()
        else:
            raise Exception('Unsupported file format!')
        return data


my_txt_writer = FileWriter('data.txt', file_data=None)
my_txt_writer.file_writer()


my_json_writer = FileWriter('data.json', file_data={'Surname': 'Zakamura', 'Country': 'Japan', 'City': 'Tokio'})
my_json_writer.file_writer()


my_csv_writer = FileWriter('data.csv', file_data=[['Yellow', 'Green', 'Pink'], ['Wolksvagen', 'BMW', 'Nissan']])
my_csv_writer.file_writer()
