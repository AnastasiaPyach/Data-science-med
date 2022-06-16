#Задание 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def func_div():
    try:
        div_1 = float(input("Введите делимое: "))
        div_2 = float(input("Введите делитель: "))
        result = div_1 / div_2
    except ValueError:
        return
    except ZeroDivisionError:
        return
    print(f'Результат деления введенных чисел равен {result:.2f}')
func_div()

