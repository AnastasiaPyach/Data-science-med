# Задание 4.Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

def my_func(x = float(input("Введите действительное положительное число: ")),
    y = int(input("Введите целое отрицательное число: "))):
    while y >= 0:
        return "Введите целое отрицательное число!"
    else:
        if y < 0:
            y = abs(y)
            x = 1 / (x * y)
        return x
print(my_func())

