from math import gcd
n, k = [int(i) for i in input().split()]
cnt = 0
for i in range(10**(k-1), 10**k):
    if gcd(n, i) == 1:
        print(i, end = " ")
        cnt += 1
    if cnt == 10:
        print()
        cnt = 0
  