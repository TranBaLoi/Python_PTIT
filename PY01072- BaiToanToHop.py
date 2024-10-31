from itertools import combinations
n, k = [int(i) for i in input().split()]
comb =  combinations(sorted({int(i) for i in input().split()}), k)
for i in list(comb):
    print(*i)