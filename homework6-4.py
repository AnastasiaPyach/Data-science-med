'''
Задание 4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
'''

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"Car {self.name} is go."
    def stop(self):
        return f"Car {self.name} is stop."
    def turn_right(self):
        return f"Car {self.name} turned right."
    def turn_left(self):
        return f"Car {self.name} turned left."
    def turn_turn(self):
        return f"Car {self.name} turned in the opposite direction."
    def show_speed(self):
        return f"Current speed of {self.name} is {self.speed} km/h."
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed} km/h.")
        if self.speed > 60:
            return f"Speed of {self.name} exceeded - {self.speed} km/h!"
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        print(f"Current speed of {self.name} is {self.speed} km/h.")
        if self.speed > 40:
            return f"Speed of {self.name} exceeded - {self.speed} km/h!"
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
Opel = TownCar(80, 'green', 'Opel', False)
Ford = SportCar(120, 'black', 'Ford', True)
Honda = WorkCar(40, 'black', 'Honda', True)
Chevrolet = PoliceCar(90, 'white and blue', 'Chevrolet', False)
print(f"Color of {Opel.name} is {Opel.color}.")
print(f"{Opel.show_speed()}")
print(f"{Ford.turn_turn()} {Ford.show_speed()}")
print(f"{Honda.go()}")
print(f"Color of Сhevrolet is black? - {Chevrolet.is_police}.")





