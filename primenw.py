# Loop through numbers from 1 to 300
for num in range(1, 301):
    if num < 2:  # Skip numbers less than 2
        continue

    # Assume the number is prime
    is_prime = True

    # Check divisors using a nested loop
    for i in range(2, num):
        if num % i == 0:  # If divisible, not a prime number
            is_prime = False
            break  # Exit the inner loop as it's not a prime number

    # If still prime, print the number
    if is_prime:
        print(num, end=" ")

    #--




"""
# Program to print all prime numbers from 1 to 300

# Loop through numbers from 2 to 300
for num in range(2, 301):  # Starting from 2 since 1 is not prime
    is_prime = True  # Flag to determine if the number is prime
    
    # Check divisors from 2 to sqrt(num)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:  # If divisible, it's not a prime number
            is_prime = False
            break  # Exit the inner loop early
    
    if not is_prime:
        continue  # Skip printing if the number is not prime
    
    print(num)  # Print the prime number
"""