# from math import a
def check(s):
    tmp = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(tmp[i]) - ord(tmp[i-1])):
            return False
    return True

for t in range(int(input())):
    s = input()
    print("YES" if check(s) else "NO")