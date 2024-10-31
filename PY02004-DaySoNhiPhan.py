
n = input()
lst = [int(j) for j in input().split()]

cnt = 0
for i in range(1,len(lst)):
    if lst[i] != lst[i-1]:
        cnt += 1
print(cnt)