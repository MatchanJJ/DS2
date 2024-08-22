import math
#number 1 ni
def fibonacchi(n1, n2, nterm):
    n3 = (n1) + n2
    if nterm == 1 or nterm == 2:
        print('1')
    elif nterm != 3:
        fibonacchi(n2, n3, nterm - 1)
    if nterm == 3:
        print(n3)
#fibonacchi(1, 1, 10)
#number 2 ni
#print(harmonic_series(0, 2))

def harmonic_series(n, nterm):
    if nterm != 0:
        n += (1/nterm)
        return harmonic_series(n, nterm-1)
    return n
#number 3 ni
def prob3(n, nterm):
    if nterm != 0:
        n += (nterm)
        return prob3(n, nterm-1)
    return n
#print(prob3(0, 5))
#number 4
def GCD(n1, n2):
    if (n1%n2) != 0:
        n3 = n1 % n2
        return(GCD(n2, n3))
    return n2
#print(GCD(1000000, 17))

#number 5 ni
def hail_stone(n):
    print(n)
    if n == 1:
        return n
    if(n%2) == 0:
        n = n/2
        return hail_stone(n)
    if (n%2) != 0:
        n = (n*3)+1
        return hail_stone(n)

hail_stone(10)


