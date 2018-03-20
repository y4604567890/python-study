# Copy from https://docs.python.org/3/tutorial/controlflow.html#defining-functions

# Fibonacci series:
# the sum of two elements defines the next
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

f = fib
print(f)
f(2000)
