from math import sqrt
def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

lst = [0, 2]
k = 3
while len(lst) <= 1000:
    if isPrime(k):
        lst += [k]
    k += 1

n, x = [int(i) for i in input().split()]
for i in range(n + 1):
    x = x + lst[i]
    print(x, end = ' ')
  