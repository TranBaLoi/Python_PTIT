import math
for i in range(int(input())):
    n, x, m = [float(j) for j in input().split()]
    x /= 100
    print(math.ceil(math.log(m / n, 1 + x)))