s = input()
while len(s) % 3 != 0:
    s = '0' + s

k = 0
lst = []
while k + 3 <= len(s):
    lst.append(s[k:k+3])
    k += 3
out = ''
for i in lst:
    out += str(int(i[0])*4 + int(i[1])*2 + int(i[2])*1)
print(out)