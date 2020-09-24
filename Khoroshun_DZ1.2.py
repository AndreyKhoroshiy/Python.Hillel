value = str(input("Введите месяц"))
if value == "01" or value == "Январь":
    print("31")
elif value == "02" or value == "Февраль":
    print("28")
elif value == "03" or value == "Март":
    print("31")
elif value == "04" or value == "Апрель":
    print("30")
elif value == "05" or value == "Май":
    print("31")
elif value == "06" or value == "Июнь":
    print("30")
elif value == "07" or value == "Июль":
    print("31")
elif value == "08" or value == "Август":
    print("31")
elif value == "09" or value == "Сентябрь":
    print("30")
elif value == "10" or value == "Октябрь":
    print("31")
elif value == "11" or value == "Ноябрь":
    print("30")
elif value == "12" or value == "Декабрь":
    print("31")
else:
    print("Вы ввели некорректные данные.Введите порядковый номер месяца в формате-01,либо название в формате-Январь")
