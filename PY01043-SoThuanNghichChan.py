for t in range(int(input())):
    n = int(input())
    for i in range(22, n, 22):
        if len(str(i)) % 2 == 1 or'1' in str(i) or '3' in str(i) or '5' in str(i) or '7' in str(i) or '9' in str(i):
            continue
        if str(i) == str(i)[::-1]:
            print(i, end =" ")
    print()