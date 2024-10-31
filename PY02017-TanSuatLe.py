import collections
for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    res = collections.Counter(lst)
    for x in res.keys():
        if res[x] % 2 == 1:
            print(x)
            break