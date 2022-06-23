# Задание 2.Создать текстовый файл (не программно),
# сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open("file2.txt", "r") as file:
    lines = 0
    words = 0
    for line in file:
        lines += 1
        words += len(line.split())
print(f"Количество строк в файле: {lines},количество слов в файле: {words}")
