number = int(input("Enter positive integer: "))
if number <= 0:
    print("Enter positive integer!")

else:
    x = 0
    for i in str(number):
        while int(i) > x:
            x = int(i)
    print(f"The largest digit in a number: {x}.")
