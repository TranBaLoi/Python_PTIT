from math import factorial
for t in range(int(input())):
    n = input()
    lst = [int(i) for i in n]
    sum = 0
    for i in lst:
        sum += factorial(i)
    print("Yes" if sum == int(n) else 'No')