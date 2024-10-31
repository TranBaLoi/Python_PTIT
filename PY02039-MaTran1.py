n = int(input())
a = []
for i in range(n):
    row = [int(i) for i in input().split()]
    a.append(row)
k = int(input())
sum_top, sum_bot = 0, 0
for i in range(n):
    for j in range(n):
        if i > j:
            sum_bot += a[i][j]
        elif i < j:
            sum_top += a[i][j]
print("YES" if abs(sum_bot - sum_top) <= k else 'NO')
print(abs(sum_bot - sum_top))
