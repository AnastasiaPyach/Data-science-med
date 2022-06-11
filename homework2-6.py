# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. ...
# Структуру нужно сформировать программно, запросив все данные у пользователя.
# Нужно собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.
goods = []
answer = []
name = None
price = 0
num = 0
ed = None
count = 0
analytics = {'name': [], 'price': [], 'num': [], 'ed': []}
while input("Если вы хотите добавить товар, ответьте 'да': ") != 'да':
    break
else:
    number = int(input("Введите количество наименований: "))
    if number <= 0:
        print("Количество наименований не может быть меньше или равно нулю.")
    while count < number:
        characteristics = {}
        for i in range(number):
            characteristics['name'] = (input("Введите название товара: "))
            characteristics['price'] = (input("Введите цену товара: "))
            characteristics['num'] = (input("Введите количество товара: "))
            characteristics['ed'] = (input("Введите единицу измерения: "))
            goods = tuple([count+1, characteristics])
            answer.append(goods)
            count += 1
            analytics['name'].append(characteristics['name'])
            analytics['price'].append(characteristics['price'])
            analytics['num'].append(characteristics['num'])
            analytics['ed'].append(characteristics['ed']) # Здесь не стала объединять одинаковые значения как в примере,
        print(*answer, sep='\n')                          # так как это может спутать пользователя
        for key in analytics:
            print(key, analytics[key])
