# Задание 7.Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

import json
summ_profit = 0
dict = {}
average_profit = {}
count = 0
with open("file7.txt", "r") as file:
    for line in file:
        name, own, proceeds, costs = line.split()
        profit = float(proceeds) - float(costs)
        if profit > 0:
            summ_profit += profit
            dict[name] = profit
            count += 1
        elif profit == 0:
            dict[name] = f'фирма работает без прибыли'
        else:
            dict[name] = f'фирма работает с убытком - {profit}'
    aver_profit = summ_profit / count
    average_profit["Средняя прибыль"] = aver_profit
print(dict, average_profit)
with open("file7.json", "w") as file_json:
    dict.update(average_profit)
    json.dump(dict, file_json)
js = json.dumps(dict)
print(js)