def check():
    lst = list(int(i) for i in input())
    for i in range(1, len(lst)):
        if abs(lst[i] - lst[i-1]) != 2:
            return False
    if sum(lst) % 10 != 0:
        return False
    return True

for t in range(int(input())):
    print("YES" if check() else "NO")