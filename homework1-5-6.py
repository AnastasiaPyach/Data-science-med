#Задание 5-6. Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма.
#Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
#Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки.
#Это отношение прибыли к выручке.
#Далее запросите численность сотрудников фирмы и
#определите прибыль фирмы в расчёте на одного сотрудника.

proceeds = int(input("Enter proceeds of your company: "))
costs = int(input("Enter costs of your company: "))
if proceeds > costs:
    profit = proceeds / costs
    profit_worker = int(input("How many workers in your company? "))
    profit_worker = (proceeds - costs) // profit_worker
    if profit_worker <= 0:
        print ("Your company works without profit. Insufficient funds to pay workers. ")
    else:
        print(f"Congratulate. Your company is profitable. Your profit is {profit:.3f}. Profit per 1 worker is {profit_worker}.")

elif proceeds == costs:
    print("Your company works without profit.")

else:
    print("Your company is operating at a loss.")
