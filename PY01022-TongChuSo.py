s = input()
cnt = 0
if len(s) == 1:
    print('1')
else:
    while len(s) > 1:
        s = str(sum([ord(i) - ord('0') for i in s]))
        cnt += 1
    print(cnt)