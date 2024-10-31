for t in range(int(input())):
    n, d = input().split()
    lst = [int(i) for i in input().split()]
    print(*(lst[int(d):] + lst[ : int(d)]))