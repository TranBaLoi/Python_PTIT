for t in range(int(input())):
    n, m = [int(i) for i in input().split()]
    lst = [int(i) for i in input().split()]
    lst.insert(lst.index(max(lst)), m)
    print(*list(filter(lambda x : x < 0, lst)), *list(filter(lambda x : x >= 0, lst)))