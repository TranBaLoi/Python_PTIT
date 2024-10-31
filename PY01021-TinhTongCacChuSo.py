for t in range(int(input())):
    s = input()
    res = sum([int(i) for i in s if i.isdigit()])
    print(*sorted([i for i in s if i.isalpha()]), res, sep='')