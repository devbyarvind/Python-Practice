number_1 = int(input("Enter Your First Number: "))
number_2 = int(input("Enter Your Second Number: "))
number_3 = int(input("Enter Your Third Number: "))

if number_1 == number_2 == number_3:
    print("All numbers are equal. Enter again.")
else:
    if number_1 >= number_2 and number_1 >= number_3:
        print(f"The First Number is Largest: {number_1}")
    elif number_2 >= number_1 and number_2 >= number_3:
        print(f"The Second Number is Largest: {number_2}")
    else:
        print(f"The Third Number is Largest: {number_3}")
