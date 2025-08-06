import sys

# Try to get input from arguments; default to 10 if none
n_terms = int(sys.argv[1]) if len(sys.argv) > 1 else 10

a, b = 0, 1
count = 0

print("Fibonacci sequence:")
while count < n_terms:
    print(a)
    a, b = b, a + b
    count += 1
