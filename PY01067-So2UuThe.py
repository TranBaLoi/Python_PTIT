for t in range(int(input())):
    s, cnt, n = [ '1', '2'], 0, int(input())
    while cnt < n:
        tmp = s[0]
        if tmp.count('2') * 2 >= len(tmp) + 1:
            print(tmp, end=' ')
            cnt += 1
        s.append(tmp + '0')
        s.append(tmp + '1')
        s.append(tmp + '2')
        del s[0]
    print()