# Get a number from the user
num = int(input("Enter a number: "))

# Handle special cases
if num <= 1:
    print(num, "is not a prime number.")
else:
    # Assume number is prime until shown otherwise
    is_prime = True
    
    # Check for factors from 2 to num-1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    
    # Print result based on is_prime
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
