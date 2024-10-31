a = []
while len(a) < 10:
    a.extend(input().split())
print(len({int(i) % 42 for i in a}))