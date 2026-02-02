num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10            # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build reversed number
    num = num // 10             # Remove last digit

print(f"The reverse of {original_num} is {reversed_num}")


# Another approach

num = input("Enter a number: ")
reversed_num = int(num[::-1])
print(f"The reverse of {num} is {reversed_num}")