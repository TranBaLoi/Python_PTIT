def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True
for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    a.sort()
    b.sort()

    print("YES" if check(a, b, n) else "NO")
# 2
# 4
# 7 5 3 2
# 5 4 8 7
# 8
# 7 5 3 2 5 105 45 10
# 2 4 0 5 6 9 75 84 
