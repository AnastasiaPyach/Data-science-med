from sys import argv

def calc_sal(time, rate, bonus):
    return float(time) * float(rate) + float(bonus)

print(calc_sal(argv[1], argv[2], argv[3]))

'''
def func_culc_sal():
    time = float(input("Введите значение выработки в часах: "))
    rate = float(input("Введите значение ставки в часах: "))
    bonus = float(input("Введите значение премии: "))
    res = time * rate + bonus
    print(f"Заработная плата сотрудника равна {res}")
func_culc_sal()
'''
