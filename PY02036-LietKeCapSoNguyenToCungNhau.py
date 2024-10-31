from math import sqrt, gcd

# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

n = int(input())
lst = sorted(int(i) for i in input().split())
for i in range(n - 1):
    for j in range(i + 1, n):
        if gcd(lst[i], lst[j]) == 1:
            print("{} {}".format(lst[i], lst[j]))
        
        
