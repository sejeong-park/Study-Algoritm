# DFS 버전 음료수 얼려먹기
n, m = map(int, input().split())
array = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True # 방문처리
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == False and array[nx][ny] == 0:
                visited[nx][ny] = True
                dfs(nx,ny)


# 모든 노드에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if visited[i][j] == False and array[i][j] == 0:
            dfs(i,j)
            result +=1

print(result)