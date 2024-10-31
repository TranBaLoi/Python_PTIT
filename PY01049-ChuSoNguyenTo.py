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
    cnt = 0
    for i in s:
        if isPrime(int(i)):
            cnt += 1
    print("YES" if cnt > len(s) - cnt and isPrime(len(s)) else "NO")