def check():
    s = input()
    if len(s) < 3:
        return False
    flag = 0
    for i in range(1,len(s)):
        if s[i] <= s[i-1]:
            flag = i - 1 
            break
    if flag == 0:
        return False
    for i in range(flag + 1, len(s)):
        if s[i] >= s[i-1]:
            return False
        
    return True

for t in range(int(input())):
    print("YES" if check() else "NO")