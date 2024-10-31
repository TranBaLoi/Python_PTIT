for i in range(int(input())):
    s = input()
    cnt = s.count('4') + s.count('7')
    print("YES" if cnt == len(s) else "NO")