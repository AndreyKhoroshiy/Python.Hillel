def get_domains():
    my_list_domains = []
    for i in open(r"C:\Users\Тарас\Python.Hillel\Homeworks\domains.txt", 'r'):
        my_list_domains.append(i[1:-1])
    return my_list_domains


print(get_domains())
##################################################################################
def get_names():
    my_list_names = []
    new_list = []
    for i in open(r"C:\Users\Тарас\Python.Hillel\Homeworks\names.txt", 'r'):
        my_list_names.append(i[:-1])
    for index in my_list_names:
        new_list.append(index.split()[1])
    return new_list


print(get_names())
###################################################################################
