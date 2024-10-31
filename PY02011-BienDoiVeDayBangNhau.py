n = int(input())
lst = [int(i) for i in input().split()]
step, res = 1e6, 1e6
for i in lst:
    s = sum(abs(i - j) for j in lst)
    if s < step:
        step = s
        res = i
print(f'{step} {res}')