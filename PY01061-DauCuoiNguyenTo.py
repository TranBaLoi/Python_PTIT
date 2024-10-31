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
    first = int(n[0:3])
    last = int(n[len(n)-3 : len(n)])
    print("YES" if isPrime(first) and isPrime(last) else "NO")