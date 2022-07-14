'''
Задание 7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
'''
class Complex_numbers:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex_numbers(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return Complex_numbers(self.a * other.a, self.b * other.b)
    def __str__(self):
        return f"{self.a}+{self.b}*j"
a = Complex_numbers(1, 2)
b = Complex_numbers(1, 2)
print(a + b)
print(a * b)