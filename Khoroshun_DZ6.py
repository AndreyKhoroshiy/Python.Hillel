my_list = ["web", "srt", "ibm", "pto", "img", "wtf", "klw", "mto"]
new_list = []
for index, value in enumerate(my_list):
    if index % 2 != 0:
        value = value[::-1]
        new_list.append(value)
    else:
        new_list.append(value)
print(new_list)
######################################################################
