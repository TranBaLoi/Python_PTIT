s = input()
while len(s) % 3 != 0:
    s = '0' + s
i = 0
res = []
while i < len(s):
    res.append(s[i:i+3])
    i += 3
tmp = ''
for x in res:
    cnt = 0
    for i in range(len(x)):
        if x[i] == '1':
            cnt += 2**(3-1-i)
    tmp += str(cnt)
print(tmp)