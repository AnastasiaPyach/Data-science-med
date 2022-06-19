from itertools import count
w = int(input("Введите число, с которого начнется отсчет: "))
y = int(input("Введите число, которым закончится отсчет: "))
for x in count(w):
    if x <= y:
        print(x)
    if x > y:
        break

from itertools import cycle
my_list = ['Пятачок', 'Винни-пух', 'Кролик']
a = int(input("Введите число, на котором Вы хотите остановить список: "))
b = 0
for el in cycle(my_list):
    if b < a:
        b +=1
        print(el)
    else:
        break