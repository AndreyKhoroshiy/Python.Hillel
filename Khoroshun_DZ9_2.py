
def reading_data():
    with open("authors.txt", "r") as authors:
        authors_list = [line.rstrip().strip('.') for line in authors.readlines()]
        new_authors_list = []
        final_list = []
        for elem in authors_list:
            if elem.isalpha():
                pass
            else:
                new_authors_list.append(elem)
        new_authors_list = list(filter(None, new_authors_list))
        word1 = "birthday"
        word2 = "death"
        word3 = "Birthday"
        word4 = "died"
        word5 = "Anne"
        for elem in new_authors_list:
            if word1 in elem:
                final_list.append(elem)
        for elem in new_authors_list:
            if word2 in elem:
                final_list.append(elem)
        for elem in new_authors_list:
            if word3 in elem:
                final_list.append(elem)
        for elem in new_authors_list:
            if word4 in elem:
                final_list.append(elem)
        for elem in final_list:
            if word5 in elem:
                final_list.remove(elem)
        # print(final_list)
        return final_list


reading_data()


finals_list = reading_data()


def replacements_of_the_month():
    result_list1 = [elem.replace("January", "01") for elem in finals_list]
    result_list2 = [elem.replace("February", "02") for elem in result_list1]
    result_list3 = [elem.replace("March", "03") for elem in result_list2]
    result_list4 = [elem.replace("April", "04") for elem in result_list3]
    result_list5 = [elem.replace("May", "05") for elem in result_list4]
    result_list6 = [elem.replace("June", "06") for elem in result_list5]
    result_list7 = [elem.replace("July", "07") for elem in result_list6]
    result_list8 = [elem.replace("August", "08") for elem in result_list7]
    result_list9 = [elem.replace("September", "09") for elem in result_list8]
    result_list10 = [elem.replace("October", "10") for elem in result_list9]
    result_list11 = [elem.replace("November", "11") for elem in result_list10]
    result_list = [elem.replace("December", "12") for elem in result_list11]
    # print(result_list)
    return result_list


replacements_of_the_month()

results_list = replacements_of_the_month()


def date_formation():
    date_list = []
    for elem in results_list:
        date_list.append(elem.split('-')[0].strip(' '))
    # print(date_list)
    date_list1 = [elem.replace("st", "") for elem in date_list]
    date_list2 = [elem.replace("rd", "") for elem in date_list1]
    date_list3 = [elem.replace("th", "") for elem in date_list2]
    date_list4 = [elem.replace("nd", "") for elem in date_list3]
    final_date_list = [elem.replace(" ", "/") for elem in date_list4]
    # print(final_date_list)
    return final_date_list


date_formation()

finals_date_list = date_formation()


def name_formation():
    name_list1 = []
    name_list2 = []
    name_list3 = []
    name_list = []
    for elem in results_list:
        name_list1.append(elem.split('-')[1].strip(' '))
    for elem in name_list1:
        name_list2.append(elem.split("'s")[0])
    for elem in name_list2:
        name_list3.append(elem.split(" d")[0])
    # print(name_list3)
    for elem in name_list3:
        name_list.append(elem.split("P ")[-1])
    # print(name_list)
    return name_list


name_formation()

names_list = name_formation()


def creat_list_dict2():
    for

dict(zip(keys, values))
#   names_list:
# finals_date_list:



lists_dict2 = creat_list_dict2()


def creat_list_dict3():
    list_dict = [dict(name=name, date=date) for name, date in zip(names_list, finals_date_list)]
    # print(list_dict)
    return list_dict


lists_dict3 = creat_list_dict3()

