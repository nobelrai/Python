# Simple Fibonacci series generator

# Number of terms you want
n_terms = int(input("How many terms? "))

# First two terms
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive number.")
elif n_terms == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n_terms:
        print(a)
        a, b = b, a + b
        count += 1
