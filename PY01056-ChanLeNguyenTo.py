from math import sqrt
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True

def check(n):
    for i in range(len(n)):
        if i % 2 == 0:
            if int(n[i]) % 2 != 0:
                return False
        if i % 2:
            if int(n[i]) % 2 == 0:
                return False
    return True
for t in range(int(input())):
    n = input()
    lst = list(int(i) for i in n)
    print("YES" if isPrime(sum(lst)) and check(n) else "NO")