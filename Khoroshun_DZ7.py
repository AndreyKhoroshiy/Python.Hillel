from random import randint
my_list = [randint(1, 100) for i in range(20)]
print(my_list)
############################################################
import random
triangle = dict(A=(random.randrange(200), random.randrange(200)),
                B=(random.randrange(200), random.randrange(200)),
                C=(random.randrange(200), random.randrange(200)))
print(triangle)
#############################################################
my_str = "I'm the string"
def my_function(my_str):
    print("***" + my_str + "***")
my_function(my_str)
#############################################################
my_dict_1 = dict(Возраст=33, Фамилия="Хорошун", Имя="Андрей", Отчество="Владимирович")
my_dict_2 = dict(Фамилия="Хорошун", Имя="Андрей", Проживание="Днепр", Работа="Есть")
my_set1 = set(my_dict_1)
my_set2 = set(my_dict_2)
my_set = my_set1.intersection(my_set2)
my_list = list(my_set)
print(my_list)
##############################################################
my_dict_1 = dict(Возраст=33, Фамилия="Хорошун", Имя="Андрей", Отчество="Владимирович")
my_dict_2 = dict(Фамилия="Хорошун", Имя="Андрей", Проживание="Днепр", Работа="Есть")
my_list = []
my_set1 = set(my_dict_1)
my_set2 = set(my_dict_2)
for i in my_set1:
    if (i in my_set1) != (i in my_set2):
        my_list.append(i)
print(my_list)
###############################################################
my_dict_1 = dict(Возраст=33, Фамилия="Хорошун", Имя="Андрей", Отчество="Владимирович")
my_dict_2 = dict(Фамилия="Хорошун", Имя="Андрей", Проживание="Днепр", Работа="Есть")
my_dict = {}
for key, value in my_dict_1.items():
    if (key in my_dict_1) != (key in my_dict_2):
        my_dict.setdefault(key, value)
print(my_dict)
################################################################