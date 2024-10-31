for i in range(int(input())):
    lst = list(int(j) for j in input())
    print("NO" if lst[0] != lst[len(lst) - 2]
          or lst[1] != lst[len(lst) - 1] else "YES")