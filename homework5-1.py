# Задание 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

with open("file1.txt", "w") as my_file:
    while True:
        text = input("Введите Ваше сообщение: ")
        my_file.write(text + '\n')
        if text == '':
            break
with open("file1.txt", "r") as file:
    for line in file:
        print(line, end="")
