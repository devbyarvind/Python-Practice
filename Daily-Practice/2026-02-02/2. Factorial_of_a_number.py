number_fact = int(input("Enter a Number To Check the Fact: "))
if number_fact < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial_num = 1
    for i in range(1, number_fact + 1):
        factorial_num *= i
    print(f"The Factorial of {number_fact} is {factorial_num}")
