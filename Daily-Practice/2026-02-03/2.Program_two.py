# Write a Python program to take numbers separated by commas from the user, convert them into integers, and store them in a list.
user_input = input("Enter the Number: ").split(",")
user_input_new = list(map(int, user_input))
print(user_input_new)