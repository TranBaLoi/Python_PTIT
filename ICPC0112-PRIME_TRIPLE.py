from math import sqrt
N = 10 ** 6
prime = [1] * (N + 5)
lst = []
def isPrime():
    prime[0] = prime[1] = 0
    for i in range(2, int(sqrt(N)) + 1):
        if prime[i] == 1:
            for j in range(i * i, N, i):
                prime[j] = 0
    for i in range(2, N):
        if prime[i] == 1:
            lst.append(i)

isPrime()
for t in range(int(input())):
    n = int(input())
    res = 0
    i = 1
    while lst[i] <= n and lst[i + 1] <= n:
        if ((lst[i] - lst[i-1] == 2 and lst[i+1] - lst[i-1] == 6)
        or (lst[i] - lst[i-1] == 4 and lst[i+1] - lst[i-1] == 6)):
            res += 1
        i += 1
    print(res)
