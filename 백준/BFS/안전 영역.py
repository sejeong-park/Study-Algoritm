# 2468 - 안전영역
from collections import deque
import sys
n = int(input())

# 초기 리스트 입력
array = []
max_value = -1e9
for _ in range(n):
    element = list(map(int, input().split()))
    array.append(element)
    max_value = max(max_value, max(element))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,k, visited):
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if array[nx][ny] > k:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    # x, y = nx, ny

result = 0
for k in range(max_value):
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and array[i][j] > k:
                bfs(i,j,k, visited)
                cnt+=1

    if result<cnt:
        result = cnt


print(result)