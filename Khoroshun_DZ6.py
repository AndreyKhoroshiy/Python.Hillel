my_list = ['web', 'srt', 'ibm', 'pto', 'img', 'wtf', 'klw', 'mto']
new_list = []
for index, value in enumerate(my_list):
    if index % 2 != 0:
        value = value[::-1]
        new_list.append(value)
    else:
        new_list.append(value)
print(new_list)
######################################################################
my_list = ['web', 'art', 'ibm', 'ato', 'img', 'atf', 'klw', 'mto']
new_list = []
for string in my_list:
    if string[0] == 'a':
        new_list.append(string)
print(new_list)
######################################################################
my_list = ['avp', 'srt', 'ibm', 'mao', 'ima', 'wtf', 'klw', 'mta']
new_list = []
for string in my_list:
    if 'a' in string:
        new_list.append(string)
print(new_list)
#######################################################################
my_list = [45, 'srt', 15, 'mao', 'ima', 84, 'klw', 'mta']
new_list = []
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)
#######################################################################
my_str = 'Andrey Khoroshun'
new_str = set(my_str)
my_list = list(new_str)
print(my_list)
#######################################################################
my_str1 = 'Andrey'
my_str2 = 'Khoroshun'
set1 = set(my_str1)
set2 = set(my_str2)
sum_set = set1.intersection(set2)
my_list = list(sum_set)
print(my_list)
#######################################################################
my_str1 = 'Andrey'
my_str2 = 'Khoroshun'
list1 = []
list2 = []
for symbol in my_str1:
    if my_str1.count(symbol) == 1:
        list1.append(symbol)
for symbol in my_str2:
    if my_str2.count(symbol) == 1:
        list2.append(symbol)
my_set1 = set(list1)
my_set2 = set(list2)
new_list = list(my_set1.intersection(my_set2))
print(new_list)
#######################################################################
Person_Khoroshun = {'Фамилия': 'Хорошун',
          'Имя': 'Андрей',
          'Возраст': 32,
          'Проживание': {
              'Страна': 'Украина',
              'Город': 'Днепр',
              'Улица': 'Фестивальный'
          },
          'Работа': {
              'Наличие': 'Есть',
              'Должность': 'Начальник участка'
          },
}
print(Person_Khoroshun['Проживание'])
######################################################################
Коржи = {
    'Мука': 1000,
    'Молоко': 300,
    'Масло': 120,
    'Яйцо': 5
}
Крем = {
    'Сахар': 450,
    'Масло': 120,
    'Ваниль': 10,
    'Сметана': 700
}
Глазурь = {
    'Какао': 200,
    'Сахар': 100,
    'Масло': 50,
}
Составляющие = {
    'Коржи': Коржи,
    'Крем': Крем,
    'Глазурь': Глазурь,
}
print(Составляющие['Коржи'])