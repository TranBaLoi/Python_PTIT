from math import sqrt

def isPrime(n):
    if n < 2:
        return 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return 1

n, m = input().split()
lst = []
for i in range(int(n)):
    row = [isPrime(int(j)) for j in input().split()]
    lst.append(row)
for i in lst:
    print(*i)

