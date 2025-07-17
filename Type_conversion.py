# Ask the user to enter a number
num = input("Enter a number: ")  # This is always a string

# Show the type before conversion
print("Before conversion, type of num is:", type(num))

# Convert to integer
num_int = int(num)
print("After converting to int:", num_int)
print("Type of num_int is:", type(num_int))

# Convert to float
num_float = float(num)
print("After converting to float:", num_float)
print("Type of num_float is:", type(num_float))

# Convert back to string
num_str = str(num_int)
print("After converting back to string:", num_str)
print("Type of num_str is:", type(num_str))
