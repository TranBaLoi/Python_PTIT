while True:
    n = int(input())
    if n == 0:
        break
    a = [n]
    while n != 1:
        if not n % 2:
            n /= 2
        else:
            n = n * 3 + 1
        a += [n]
    print(len({int(i) for i in a}))