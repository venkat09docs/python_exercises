# write a function for fibonacci sequence

def fibonacci(n):
    """Generate Fibonacci sequence up to the n-th term."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

a, b = 4, 5
x, y = '4', '5'

print(f"Sum of integers: {a > b}")
print(f"Sum of Srings: {x + y}")

print(a.__add__(b))
print(x.__add__(y))