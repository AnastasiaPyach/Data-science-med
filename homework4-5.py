from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f"Список четных элементов в списке от 100 до 1000: {my_list}")
def my_func(prev_el, el):
    return prev_el * el
print(f"Результат произведения всех элементов в списке: {reduce(my_func, my_list)}")
