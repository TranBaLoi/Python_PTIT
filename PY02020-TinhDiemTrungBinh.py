n = int(input())
lst = [float(i) for i in input().split()]
cou_min = min(lst)
cou_max = max(lst)

for i in lst:
    if i == cou_max or i == cou_min:
        lst.remove(i)
print('{:.2f}'.format(sum(lst) / len(lst)))