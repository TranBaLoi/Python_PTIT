alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for t in range(int(input())):
    n, k = [int(i) for i in input().split()]
    res = ''
    while n > 0:
        res += alpha[n%k]
        n //= k
    print(res[::-1])