'''
Задание 1.  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year
    def __str__(self):
        return self.day_month_year
    @classmethod
    def number(cls, data):
        print(*map(int, data.split('-')), sep='/')
    @staticmethod
    def valid(day, month, year):
        if 0 < day <= 31:
            if 0 < month < 12:
                if year == 2022:
                    return f"Today is {day}-{month}-{year}"
                else:
                    return f"Wrong year"
            else:
                return f"Wrong month"
        else:
            return "Wrong day"

data = Data("13-07-2021")
print(data)
print(Data.number('10-09-2001'))
print(data.number('13-07-2022'))
print(data.valid(13, 7, 2022))
print(Data.valid(10, 7, 2020))