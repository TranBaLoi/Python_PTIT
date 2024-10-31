n, m = [int(i) for i in input().split()]
matrix = [[int(i) for i in input().split()] for j in range(n)]
cnt = 0
vs = [[False for j in range(m)] for i in range(n)]
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
for i in range(n):
    for j in range(m):
        if matrix[i][j] == -1:
            for k in range(8):
                if i + dx[k] >= 0 and j + dy[k] >= 0 and i + dx[k] < n and j + dy[k] < m and vs[i + dx[k]][j + dy[k]] == False:
                    cnt += matrix[i + dx[k]][j + dy[k]]
                    vs[i + dx[k]][j + dy[k]] = True
print(cnt)
                    

                    
