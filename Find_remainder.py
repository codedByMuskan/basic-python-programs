# Ask the user to enter a number
num = int(input("Enter the number: "))

# Ask the user to enter the divisor (z)
z = int(input("Enter the number to divide by (z): "))

# Find the remainder using the modulus operator %
remainder = num % z

# Print the result
print("The remainder when", num, "is divided by", z, "is", remainder)
