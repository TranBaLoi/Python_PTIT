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
        if isPrime(i):
            if n[i] != '2' and n[i] != '3' and n[i] != '5' and n[i] != '7':
                return False
        else:
            if n[i] == '2' or n[i] == '3' or n[i] == '5' or n[i] == '7':
                return False
    return True

for t in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")
