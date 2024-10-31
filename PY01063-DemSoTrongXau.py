for t in range(int(input())):
    s = input()
    n = input()
    l , idx, cnt = len(n), s.find(n), 0
    while idx != -1:
        cnt += 1
        idx = s.find(n, idx + l, len(s))
    print(cnt)
        