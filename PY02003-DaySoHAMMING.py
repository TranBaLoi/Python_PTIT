lst = []
N = 10 ** 18

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            lst += [i * j * k]
            k *= 5
        j *= 3
    i *= 2
lst.sort()

def binarySearch(l, r, x):
    if l > r:
        return "Not in sequence"
    mid = (l + r) // 2
    if lst[mid] == x:
        return mid + 1
    if lst[mid] > x:
        return binarySearch(l, mid - 1, x)
    return binarySearch(mid + 1, r, x)

for t in range(int(input())):
    n = int(input())
    print(binarySearch(0, len(lst), n))