# Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_list_num = ['Один', 'Два', 'Три', 'Четыре']
new_list_num = []
with open("file4.txt", "r", encoding = "utf-8") as file:
    for el in range(len(my_list_num)):
        for line in file:
            line = line.split(' ', 1)
            a = new_list_num.append(my_list_num[el] + " " + line[1])
            el += 1
    print(new_list_num)
with open("file4_1.txt", 'w') as file_1:
    file_1.writelines(new_list_num)
