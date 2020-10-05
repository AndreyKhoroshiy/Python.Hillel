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
