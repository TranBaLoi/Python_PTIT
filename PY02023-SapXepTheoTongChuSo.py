for t in range(int(input())):
    n = int(input())
    lst = [i for i in input().split()]
    lst.sort(key=lambda x : (sum(int(i) for i in x), int(x)))
    print(*lst)