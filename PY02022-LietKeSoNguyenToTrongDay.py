from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

mark, tmp = {}, []
n = int(input())
lst = [int(i) for i in input().split()]
for i in lst:
    if i in tmp:
        mark[i] += 1
        continue
    elif isPrime(i) :
        mark[i] = 1
        tmp += [i]
for i in tmp:
    print('{} {}'.format(i, mark[i]))

