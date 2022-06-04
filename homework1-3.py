#Задание 3.Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

number = int(input("Enter number: "))
number2 = int(str(number) + str(number))
number3 = int(str(number) + str(number) + str(number))

sum = number + number2 + number3
print(f"Sum of numbers {number} + {number2} + {number3} is {sum} .")