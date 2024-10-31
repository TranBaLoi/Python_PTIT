def mul(x):
    res = 1
    for i in x:
        res *= int(i)
    return res


for t in range(int(input())):
    n = int(input())
    lst = [i for i in input().split()]
    tich = 1
    lst.sort(key=lambda x : (mul(x), int(x)))
    print(*lst)