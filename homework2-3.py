# Задание 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'January', 2: 'February',
                3: 'March', 4: 'April', 5: 'May',
                6: 'June', 7: 'July', 8: 'August',
                9: 'September', 10: 'October', 11: 'November',
                12: 'December'}
month = int(input("Введите месяц в виде целого числа: "))
if month == 1 or month == 2 or month == 12:
    print(f"Your season is {seasons_list[0]} and your month is {seasons_dict[month]}")
elif month == 3 or month == 4 or month == 5:
    print(f"Your season is {seasons_list[1]} and your month is {seasons_dict[month]}")
elif month == 6 or month == 7 or month == 8:
    print(f"Your season is {seasons_list[2]} and your month is {seasons_dict[month]}")
elif month == 9 or month == 10 or month == 11:
    print(f"Your season is {seasons_list[3]} and your month is {seasons_dict[month]}")
else:
    print("Такого месяца нет")
