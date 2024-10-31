def check(lst = []):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True
for t in range(int(input())):
    lst = list(int(i) for i in input())
    print("YES" if check(lst) else "NO")