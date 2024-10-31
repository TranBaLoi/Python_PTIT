from math import comb
n = int(input())
matrix = []
row = [0] * n
col = [0] * n
for i in range(n):
    matrix += [[i for i in input()]]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
       if matrix[i][j] == 'C':
           row[i] += 1
           col[j] += 1
cnt = 0
for i in range(n):
    cnt += comb(row[i], 2)
    cnt += comb(col[i], 2)
print(cnt)
# 4
# CC..
# C..C
# .CC.
# .CC.