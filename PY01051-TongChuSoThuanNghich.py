def check(n):
    if n == n[::-1] and len(n) > 1:
        return True
    return False

for t in range(int(input())):
    lst = list(int(i) for i in input())
    print("YES" if check(str(sum(lst))) else "NO")