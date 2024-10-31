p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    Input = input()
    if Input == '0':
        break
    else:
        k, s = Input.split()
        k = int(k)
        s1 = ''
        for i in range(len(s)):
            j = p.find(s[i])
            s1 += p[(j + k) % 28]
        print(s1[::-1])