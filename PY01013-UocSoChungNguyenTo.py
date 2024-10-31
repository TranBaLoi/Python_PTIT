import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    gcd = math.gcd(a, b)
    lst = list(int(x) for x in str(gcd))
    print("YES" if isPrime(sum(lst)) else "NO")