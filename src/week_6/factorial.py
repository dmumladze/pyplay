
def factorial_loop(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def factorial_recursive(n):
    if n == 1:
        return 1
    factorial = factorial_recursive(n-1)
    prod = n * factorial
    print(n, "*", factorial, "=", prod, sep='')
    return prod   

print(factorial_loop(5))
print(factorial_recursive(5))