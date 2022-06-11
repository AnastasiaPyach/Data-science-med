#Задание 5.Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [8, 7, 5, 2, 1]
print('Current rating is 8, 7, 5, 2 ,1')
new_el = int(input("Enter new element of rating: "))
for el in range(len(rating)):
    if rating[el] == new_el:
        rating.insert(el + 1, new_el)
        break
    elif rating[-1] > new_el:
        rating.append(new_el)
    elif rating[0] < new_el:
        rating.insert(0, new_el)
    elif rating[el] > new_el and rating[el + 1] < new_el:
        rating.insert(el + 1, new_el)
        break
print(f'Your rating is {rating}')
