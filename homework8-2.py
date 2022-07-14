'''
Задание 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
class Div_zero(Exception):
    def division_by_zero(self, txt):
        self.txt = txt
try:
    inp_dividend = input("Введите делимое: ")
    inp_divisor = input("Введите делитель: ")
    inp_dividend = float(inp_dividend)
    inp_divisor = float(inp_divisor)
    if inp_divisor != 0:
        print(f"Результат деления {inp_dividend} на {inp_divisor}: {inp_dividend / inp_divisor}")
    else:
        raise Div_zero("Делить на 0 нельзя!")
except Exception as err:
    print(err)




