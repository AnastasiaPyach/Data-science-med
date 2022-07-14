'''
Задание 3.
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
'''
class List_int:
    def __init__(self):
        self.my_list = []
        while True:
            try:
                var_list = input("Введите числовое значение, которое хотите внести в список. \n" 
                                "Для выхода из цикла введите 'stop': ")
                var_list = float(var_list)
                if isinstance(var_list, (int, float)):
                    self.my_list.append(var_list)
            except:
                if var_list == 'stop':
                    print(f"Ваш список {self.my_list}. Ввод закончен.")
                    break
                else:
                    print(f"Введено не числовое значение")

new_list = List_int()
new_list.my_list



