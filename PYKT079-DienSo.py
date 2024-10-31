for t in range(int(input())):
    n = int(input())
    lst = {int(i) for i in input().split()}
    print(max(lst) - min(lst) + 1 - len(lst))
# 2
# 5
# 4 5 3 8 6
# 3
# 2 1 3