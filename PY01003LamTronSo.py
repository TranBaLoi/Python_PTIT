t = int(input())
for x in range(0, t):
    s = input()
    a = list(int(i) for i in s)
    if len(a) == 1:
        print(s)
    else:
        for i in range(len(a) - 1, 0, -1):
            if(a[i] >= 5):
                a[i - 1] += 1
            a[i] = 0
        for i in a:
            print(i,end = '')
        print('')