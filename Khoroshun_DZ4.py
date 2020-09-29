my_list = [10, 25, 50, 110, 135, 145, 98]
for value in my_list:
    if value > 100:
        print(value)
##########################################
my_list = [10, 25, 50, 110, 135, 145, 98]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(int(value))
print(my_results)
##########################################
my_list = [10, 25, 50, 110, 135, 145, 98]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(int(my_list[-1] + my_list[-2]))
print(my_list)
##########################################
value = input("Введите число")
try:
    value = float(value)
    result = value ** -1
    print(result)
except ValueError:
    print("Не корректный ввод, Вы ввели не число")
except ZeroDivisionError:
    print("Не корректный ввод. Вероятно, Вы попытались возвести ноль в отрицательную степень")
##########################################
my_list = [10, 25, 50, 110, 135, 145, 98]
my_indexes = [0, 1, 2, 3, 4, 5, 6]
for index in my_indexes:
    print(my_list[index])
#########################################
my_list1 = [10, 25, 50, 110, 135, 145, 98]
my_list2 = [40, 56, 28, 123, 137, 159, 23]
my_indexes = [0, 1, 2, 3, 4, 5, 6]
for index in my_indexes:
    print((my_list1[index], my_list2[index]))
##########################################
my_string = '0123456789'
my_list = []
for symb_1 in my_string:
    for symb_2 in my_string:
        print(symb_1 + symb_2)
        my_list.append(int(symb_1 + symb_2))
print(my_list)
###########################################
