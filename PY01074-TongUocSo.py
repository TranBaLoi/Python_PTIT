# Bài này input output sai tùm lum

from math import sqrt
N = 10 ** 7
a = [0] * (N + 5)

def init():
    for i in range(2, int(sqrt(N)) + 1):
        for j in range(i, N + 1, i):
            if a[j] == 0 :
                a[j] = int(i)
    for i in range(2, N + 1):
        if a[i] == 0:
            a[i] = int(i)
  
def solve(n):
    if a[n] == 0:
        return n 
    sum = 0
    while n != 1:
        sum += a[n]
        n = int(n / a[n])
    return sum

init()
sum = 0
for t in range(int(input())):
    sum += solve(int(input()))
print(sum)


