for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    cnt = [1] * n
    for i in range(1, n):
        id = i - 1
        while lst[i] >= lst[id] and id >= 0:
            cnt[i] += cnt[id]
            id -= cnt[id]
    print(*cnt)