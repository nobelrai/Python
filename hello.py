# Get input from user
try:
    n_terms = int(input("Enter the number of Fibonacci terms: "))
    if n_terms <= 0:
        raise ValueError("Number of terms must be positive.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(a)
    a, b = b, a + b
    count += 1
