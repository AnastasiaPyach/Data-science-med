#Пользователь вводит время в секундах.
#Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
#Используйте форматирование строк.

time_all_sec = int(input("Enter your time in seconds: "))

time_hour = time_all_sec // 3600

time_min = (time_all_sec - (time_hour * 3600)) // 60

time_sec = (time_all_sec - (time_min * 60 + time_hour * 3600))
if time_hour == 0:
    print(f"Your time is : {time_min} min {time_sec} sec.")
else:
    print(f"Your time is : {time_hour} h {time_min} min {time_sec} sec.")




