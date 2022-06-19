my_list = [2, 3, 3, 6, 7, 8, 3, 9, 8, 56, 4, 34, 43, 34, 87]
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(my_new_list)