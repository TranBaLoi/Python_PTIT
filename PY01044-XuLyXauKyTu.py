s1 = {i.lower() for i in input().split()}
s2 = {i.lower() for i in input().split()}

print(*sorted(s1 | s2))
print(*sorted(s1 & s2))
