from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True

for t in range(int(input())):
    n = input()
    lst = list(int(i) for i in n)
    print("YES" if isPrime(sum(lst)) else "NO")