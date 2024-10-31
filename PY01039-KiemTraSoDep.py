def check() :
    n = input()
    if n.count(n[0]) + n.count(n[1]) != len(n):
        return False
    for i in range(2,len(n), 2):
        if n[i] != n[i-2]:
            return False
    for i in range(3, len(n), 2):
        if(n[i] != n[i-2]):
            return False
    return True

for t in range(int(input())):
    print("YES" if check() else "NO")