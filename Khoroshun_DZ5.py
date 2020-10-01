value = 564000000784000000007
symbol = 0
my_value = str(value)
my_symbol = str(symbol)
count = my_value.count(my_symbol)
print(count)
#######################################
value = 5640007840000000
symbol = 0
my_list = []
my_value = str(value)
my_str = my_value[::-1]
for symbol in my_str:
    if int(symbol) == 0:
        my_list.append(symbol)
    else:
        break
print(len(my_list))
########################################
my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [10, 15, 20, 25]
my_result = []
for value in my_list_1:
    if value % 2 == 0:
        my_result.append(value)
for value in my_list_2:
    if value % 2 != 0:
        my_result.append(value)
print(my_result)
########################################
