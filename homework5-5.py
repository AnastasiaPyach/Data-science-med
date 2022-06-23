# Задание 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

my_list = input("Введите числовые значения через пробел: ")
summ = 0
with open("file5.txt", "w") as my_file:
    my_file.write(my_list)
with open("file5.txt") as file:
    file_open = file.read()
    for x in file_open.split():
        summ += float(x.strip())
print(f"Сумма чисел в файле равна {summ}")
