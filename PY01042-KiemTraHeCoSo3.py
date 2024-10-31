for t in range(int(input())):
    s = input()
    total = s.count('1') + s.count('0') + s.count('2')
    print("YES" if total == len(s) else "NO")