for t in range(int(input())):
    p, q = [i for i in input().split()]
    ip = input().split()
    if len(ip) == 1:
        x1 = ip[0]
        x2 = input()
    else:
        x1, x2 = ip
    mx = max(q, p)
    mn = min(q, p)
    sum_max = int(x1.replace(mn, mx)) + int(x2.replace(mn, mx))
    sum_min = int(x1.replace(mx, mn)) + int(x2.replace(mx, mn))
    print(sum_min, sum_max)