for t in range(int(input())):
    lst = list(int(i) for i in input())
    print("NO" if  sum(lst) % 3 != 0 else "YES")