number = int(input("Enter a Digit: "))

total_sum= 0

while number>0:
    last_digit= number%10
    total_sum += last_digit
    number=number//10

print(f"The Sum of digit is {total_sum}")