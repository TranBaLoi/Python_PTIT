import math
def isPrime(s):
    kq = s[len(s) - 4 : len(s)]
    kq = int(kq)
    if kq < 2:
        return False
    for i in range(2, int(math.sqrt(kq))):
        if not kq % i :
            return False
    return True

for t in range(int(input())):
    s = input()
    print("YES" if isPrime(s) else "NO")