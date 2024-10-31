from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True

for t in range(int(input())):
    s = input()
    n = int(s[len(s)-4] + s[len(s)-3] + s[len(s)-2] + s[len(s)-1])
    print("YES" if isPrime(n) else "NO")