n = int(input())
lst = []
while True:
    tmp = [int(i) for i in input().split()]
    lst += tmp
    if len(lst) == n:
        break
odd, even, res = [], [], []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
odd = sorted(odd, key=lambda x : -x)
even = sorted(even)
for i in lst:
    if i % 2 == 0:
        res.append(even[0])
        even.pop(0)
    else:
        res.append(odd[0])
        odd.pop(0)
print(*res)