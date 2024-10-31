lst = []
for t in range(int(input())):
    lst.append(input())
print(len({i for i in lst}))