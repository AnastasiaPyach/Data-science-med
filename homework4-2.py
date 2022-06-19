my_list = [1, 5, 4, 9, 450, 36, 5, 8, 79]
my_new_list = [el for el in my_list if el > my_list[my_list.index(el) - 1]]
print(my_new_list)
