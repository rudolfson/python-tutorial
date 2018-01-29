def fib(n):
    """Print a fibonacci series up to n"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, a+b

import sys
print(sys.argv)

if len(sys.argv) == 2:
    fib(int(sys.argv[1]))
