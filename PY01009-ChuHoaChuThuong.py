s = input()
low = up = 0
for i in s:
    if i.islower():
        low += 1
    else:
        up +=1
print(s.lower() if low >= up else s.upper())