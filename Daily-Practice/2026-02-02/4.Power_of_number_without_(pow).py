base = int(input("Enter The input: "))
exponent = int(input("Enter The input: "))

power = base**exponent
print(f"This is the {power}")

# Using Function
def power_value(base_value,exponent_value):
    return base_value**exponent_value

base_value=3
exponent_value=5
print(f"This is the {power_value(base_value, exponent_value)}")