for t in range(int(input())):
    lst = [i for i in input()]
    mn = 10 ** 18
    tmp = ''
    while len(lst) != 0:
        x = lst.pop()
        if x >= '0' and x <= '9':
            tmp += x
        else:
            if tmp != '':
                mn = min(mn, int(tmp[::-1]))
            tmp = ''
    if tmp != '':
        mn = min(mn, int(tmp[::-1]))
    print(mn)