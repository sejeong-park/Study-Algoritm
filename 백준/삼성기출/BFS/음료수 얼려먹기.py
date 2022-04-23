from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == False and array[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and array[i][j] == 0:
            bfs(i,j)
            cnt+=1

print(cnt)
