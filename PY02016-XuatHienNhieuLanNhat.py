for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    mark = {}
    cou_max = 0
    val_min = max(lst)
    for i in lst:
        if i in mark:
            mark[i] += 1
        else:
            mark[i] = 1
        if cou_max < mark[i]:
            cou_max = mark[i]
            val_min = i
        elif cou_max == mark[i] and i < val_min:
            val_min = i
    print(val_min if cou_max > n / 2 else 'NO')