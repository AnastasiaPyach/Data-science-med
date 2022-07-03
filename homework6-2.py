'''
Задание 2.Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
'''

class Road:
    mass_k = 25 #примерный расход асфальта на 1 кв. м. при толщине слоя 1 см равен 25 кг
    def __init__(self, _length, _width):
        self._length = float(_length)
        self._width = float(_width)
    def square(self):
        return self._length * self._width
class Mass_asphalt(Road):
    def __init__(self, _length, _width, thickness):
        super().__init__(_length, _width)
        self.thickness = thickness
    def final_mass(self):
        return (self._length * self._width * self.thickness * self.mass_k) / 1000
r = Mass_asphalt(20, 5000, 5)
print(f"Масса асфальта, необходимая для покрытия всей дороги с заданными данными - {r.final_mass()} тонн")