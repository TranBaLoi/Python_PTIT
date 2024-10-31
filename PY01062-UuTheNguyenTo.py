from math import sqrt

def isPrime(n):
    if n < 2 :
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True

for t in range(int(input())):
    n = input()
    cnt = 0
    for i in range(len(n)):
        if isPrime(int(n[i])):
            cnt += 1
    print("YES" if isPrime(len(n)) and cnt > len(n) - cnt else "NO")