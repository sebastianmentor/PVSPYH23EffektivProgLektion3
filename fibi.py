from functools import cache

@cache
def fib(n):
    match n:
        case 0: return 1
        case 1: return 1
        case _: return fib(n-2) + fib(n-1)

print(fib(40))
