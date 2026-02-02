check_number =  int(input("Enter a Number: "))
if check_number <0:
    print(f"Given Number is Negative {check_number}")
elif check_number ==0:
    print(f"Given Number is Zero {check_number}")
else:
    print(f"Given Number is Positive {check_number}")

# Another Approach
check_number = int(input("Enter a Number: "))

if check_number < 0:
    result = "Negative"
elif check_number == 0:
    result = "Zero"
else:
    result = "Positive"

print(f"Given Number is {result}: {check_number}")