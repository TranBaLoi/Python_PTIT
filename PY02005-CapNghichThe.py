n = int(input())
lst = [int(i) for i in input().split()]
cnt = 0
for i in range(0,n-1):
    for j in range(i + 1, n):
        if lst[j] < lst[i]:
            cnt += 1
print(cnt)