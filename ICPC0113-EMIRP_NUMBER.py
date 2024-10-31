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
    i = 0
    tmp = lst.copy()
    while tmp[i] <= n:
        if (str(tmp[i]) != str(tmp[i])[::-1]
        and int(str(tmp[i])[::-1]) <= n 
        and  prime[int(str(tmp[i])[::-1])] == 1):
            print(tmp[i], int(str(tmp[i])[::-1]) , end = ' ')
            tmp.remove(int(str(tmp[i])[::-1]))
        i += 1
    print()