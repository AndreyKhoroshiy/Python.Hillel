my_list = [10, 25, 50, 110, 135, 145, 98]
for value in my_list:
    if value > 100:
        print(value)
##########################################
my_list = [10, 25, 50, 110, 135, 145, 98]
my_results = []
for value in my_list:
    if value > 100:
        my_results.append(value)
print(my_results)
##########################################
my_list = [10, 25, 50, 110, 135, 145, 98]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[-1] + my_list[-2])
print(my_list)
##########################################
