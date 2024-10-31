n = int(input())
lst = [int(i) for i in input().split()]
lst.sort()
ok = 0
for i in range(n-1):
    if lst[i+1] - lst[i] > 1:
        print(lst[i] + 1)
        ok = 1
        break
if ok == 0:
    print(lst[n-1] + 1)
