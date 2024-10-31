from itertools import permutations
per = permutations(input())
for i in list(per):
    print(''.join(i))