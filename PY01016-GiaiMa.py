for t in range(int(input())):
    s = input()
    code = ''
    for i in range(0, len(s) - 1, 2):
        code += str(s[i] * int(s[i+1]))
    print(code)