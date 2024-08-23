#fibonacci
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]
#print(fibonacci(10))
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n - 1) + fibonacci2(n - 2)
#print(fibonacci2(2))

def harmonic_series(n):
    if n == 1:
        return 1
    return 1 / n + harmonic_series(n - 1)
#print(harmonic_series(2))

def prob3(n):
    if n == 1:
        return 1
    return n + prob3(n - 1)
#print(prob3(5))

def GCD(n1, n2):
    if n2 == 0:
        return n1
    return GCD(n2, n1 % n2)
#print(GCD(12,8))

def hailstone(n):
    print(int(n))
    if n == 1:
        return n
    if n%2 == 0:
        return hailstone(n // 2)
    return hailstone(n * 3 + 1)
#hailstone(10)