from math import gcd
n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
for i in range(n-1):
    for j in range(i + 1, n):
        if gcd(lst[i], lst[j]) == 1:
            print("{} {}".format(lst[i], lst[j]))