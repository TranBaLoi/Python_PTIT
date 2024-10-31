for t in range(int(input())):
    lst = [i for i in input()]
    mn = -10 ** 17
    tmp = ''
    while len(lst) != 0:
        x = lst.pop()
        if x >= '0' and x <= '9':
            tmp += x
        else:
            if tmp != '':
                mn = max(mn, int(tmp[::-1]))
            tmp = ''
    if tmp != '':
        mn = max(mn, int(tmp[::-1]))
    print(mn)