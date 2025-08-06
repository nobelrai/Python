import sys

# Check if an argument was provided
if len(sys.argv) < 2:
    print("Usage: python hello.py <number_of_terms>")
    sys.exit(1)

# Get number of terms from the first argument
n_terms = int(sys.argv[1])

a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(a)
    a, b = b, a + b
    count += 1
