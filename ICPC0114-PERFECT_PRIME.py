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
    ok = True
    lst = [int(i) for i in n]
    for i in lst:
        if not isPrime(i):
            ok = False
    
    print("Yes" if isPrime(int(n)) and isPrime(int(n[::-1]))
        and isPrime(sum(lst)) and ok == True   else "No")