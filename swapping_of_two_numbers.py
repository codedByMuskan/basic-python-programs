# Get input from user
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swap without using a third variable
a = a + b
b = a - b
a = a - b

print(f"After swapping: a = {a}, b = {b}")
