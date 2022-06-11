# Задание 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки нужно пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

my_string = input("Enter a string divided with spaces: ")
string = my_string.split(' ')
for i, word in enumerate(string, 1):
    if len(word) > 10:
       word = word[0:10]
    print(f'{i}. {word}')