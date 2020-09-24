value = int(input("Введите целое число"))
new_value = value/2 if value < 100 else - value
print(new_value)
####################
value = int(input("Введите целое число"))
new_value = 1 if value < 100 else 0
print(new_value)
####################
value = int(input("Введите целое число"))
new_value = True if value < 100 else False
print(new_value)
####################
my_str = str(input("Введите буквы разного регистра"))
my_new_str = my_str.upper()
print(my_new_str)
#####################
my_str = str(input("Введите буквы разного регистра"))
my_new_str = my_str.lower()
print(my_new_str)
#####################
my_str = str(input("Введите строку"))
my_new_str = my_str * 2 if len(my_str) < 5 else my_str
print(my_new_str)
#####################
my_str = str(input("Введите строку"))
my_new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_new_str)
#####################
my_str = str(input("Введите строку"))
for symbol in my_str:
    if symbol in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъёфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
       print(symbol)
#####################
my_str = str(input("Введите строку"))
for symbol in my_str:
    if symbol not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъёфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ":
        print(symbol)
#####################
my_str = str(input("Введите строку"))
for symbol in my_str:
    if symbol not in "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMйцукенгшщзхъёфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ ":
       print(symbol)