for t in range(int(input())):
    lst = [int(i) for i in input()]
    if lst[len(lst) - 2] != 8 or lst[len(lst) - 1] != 6:
        print("NO")
    else:
        print("YES")