# Задание 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func():
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    c = float(input("Введите третье число: "))
    if a >= b and b > c or a < b and a > c:
        return a + b
    elif a > b and b <= c:
        return a + c
    else:
        return b + c
print(f'Сумма двух наибольших чисел равна: {my_func()}')



