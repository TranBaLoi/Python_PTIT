big = 10**9
for t in range(int(input())):
    n = int(input())
    lst = [int(i) for i in input().split()]
    min1, min2, min3 = big, big, big
    for i in lst:
        if i >= min3:
            continue
        elif i < min1:
            min3 = min2
            min2 = min1
            min1 = i
        elif i < min2:
            min3 = min2
            min2 = i
        elif i < min3:
            min3 = i
    print(min1 + min2 + min3)