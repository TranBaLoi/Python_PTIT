while True:
    n = int(input())
    if n == 0:
        break
    lst = [int(input()) for i in range(n)]
    print("BANG NHAU" if lst.count(lst[0]) == n else f'{min(lst)} {max(lst)}')
    