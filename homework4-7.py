from math import factorial
from itertools import count
def gener_fact():
    for el in count(1):
        yield factorial(el)
gen = gener_fact()
a = int(input("Введите число, факториал которого хотите получить: "))
x = 0
for el in gen:
    if x < a:
        print(el)
        x += 1
    else:
        break