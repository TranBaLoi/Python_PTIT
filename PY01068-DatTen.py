from itertools import combinations
n, k = [int(i) for i in input().split()]
lst = sorted({i for i in input().split()})
res = list(combinations(lst, k))
for i in res:
    print(*i)

    