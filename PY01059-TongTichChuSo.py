def check(s):
    sum = 0
    mul = 1
    ok = 0
    for i in range(len(s)):
        if i % 2 != 0:
            sum += int(s[i])
        elif i % 2 == 0 and int(s[i]) != 0:
            mul *= int(s[i])
            ok = 1
    print(mul if ok == 1 else 0, end = " ")
    print(sum)
for t in range(int(input())):
    check(input())