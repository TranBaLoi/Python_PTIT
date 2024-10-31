def check():
    n = input()
    if n[0] == n[1] or len(n) % 2 == 0:
        return False
    for i in range(2, len(n), 2):
        if n[i] != n[i-2]:
            return False
    return True

for t in range(int(input())):
    print("YES" if check() else "NO")