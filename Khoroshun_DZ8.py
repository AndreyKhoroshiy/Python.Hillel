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
import random


def get_number():
    return random.randrange(100, 999)


number = get_number()


def get_string():
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=(random.randrange(5, 7))))


string = get_string()


def get_domains():
    my_list_domains = []
    for i in open(r"C:\Users\Тарас\Python.Hillel\Homeworks\domains.txt", 'r'):
        my_list_domains.append(i[1:-1])
    return my_list_domains


domain = random.choice(get_domains())


def get_names():
    my_list_names = []
    new_list = []
    for i in open(r"C:\Users\Тарас\Python.Hillel\Homeworks\names.txt", 'r'):
        my_list_names.append(i[:-1])
    for index in my_list_names:
        new_list.append(index.split()[1])
    return new_list


name = random.choice(get_names())


def generate_e_mail(name, number, string, domain):
    e_mail = f'{name}.{number}@{string}.{domain}'
    print(e_mail)


generate_e_mail(name, number, string, domain)
############################################################################
