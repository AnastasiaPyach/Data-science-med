'''
Задание 4-5-6. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
...
'''
class Storage:
    def __init__(self):
        self.dict = {}
    def __str__(self):
        return f'{self.dict}'
    def take_to_Storage(self, num, equip, data):
        self.equip = equip
        self.data = data
        self.num = num
        if not isinstance(self.num, int):
            raise ValueError('Введено не числовое значение')
        self.dict.update({'Порядковый номер': self.num, 'Объект': self.equip, 'Дата поступления' : self.data})
        print(f"На склад получено оборудование: \n{self.dict}")
    def give_to(self, num, equip, data):
        self.equip = equip
        self.data = data
        self.num = int(num)
        self.dict.update({'Порядковый номер': self.num, 'Объект': self.equip, 'Дата передачи': self.data})
        print(f"Передано оборудование: \n{self.dict}")
class Office_equip:
    def __init__(self, model, amount, price):
        self.model = model
        self.amount = amount
        self.price = price
    def __str__(self):
        return f"{self.model}, {self.amount}, {self.price}"

class Printers(Office_equip):
    def __init__(self, model, amount, price, amount_of_paper):
        super().__init__(model, amount, price)
        self.amount_of_paper = amount_of_paper
    def print(self):
        if self.amount_of_paper > 0:
            return f"Принтер начал работу."
        else:
            return f"Бумага в принтере закончилась. Загрузите новую."

class Scanners(Office_equip):
    def __init__(self, model, amount, price):
        super().__init__(model, amount, price)

    def scan(self):
        return f"Сканер начал работу."

class Copiers(Office_equip):
    def __init__(self, model, amount, price, amount_of_paper):
        super().__init__(model, amount, price)
        self.amount_of_paper = amount_of_paper
    def work(self):
        if self.amount_of_paper > 0:
            return f"Ксерокс начал работу."
        else:
            return f"Бумага в ксероксе закончилась. Загрузите новую."

storage = Storage()
printer = Printers('Canon', 2, 1500, 0)
scanner = Scanners('HP', 3, 1000)
copier = Copiers('Canon', 6, 2000, 50)
storage.take_to_Storage(1, 'printer', '14.07.2022')
storage.take_to_Storage(2, 'scanner', '13.07.2022')
storage.give_to(1, 'scanner', '14.07.2022')

print(printer.print())
print(scanner.scan())
print(copier.work())