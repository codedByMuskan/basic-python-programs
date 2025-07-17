## Ask the user to enter a number
num = int(input("Enter a number: "))

# Start factorial from 1
factorial = 1

# Make a loop from 1 to the number (including the number)
for i in range(1, num + 1):
    factorial = factorial * i  # multiply factorial by i every time

# Show the answer
print("Factorial of", num, "is", factorial)
