## Ask the user how many terms to print
n = int(input("Enter the number of terms: "))

# First two terms of the Fibonacci series
a = 0
b = 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    print(a, b, end=" ")
    for i in range(2, n):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
