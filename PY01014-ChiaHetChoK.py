a, k, n = [int(i) for i in input().split()]
b = k - a % k
lst = []
for i in range(b, n - a + 1, k):
    if a + i <= n:
        lst.append(i)
if len(lst) == 0:
    print(-1)
else:
    for i in lst:
        print(i, end = " ")