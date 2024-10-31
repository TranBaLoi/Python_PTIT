n = int(input())
lst = [int(i) for i in input().split()]

i = 1
while i < len(lst):
    if (lst[i] + lst[i-1]) % 2 == 0:
        lst.pop(i)
        lst.pop(i-1)
        if i > 1:
            i -= 1
    else:
        i += 1
print(len(lst))