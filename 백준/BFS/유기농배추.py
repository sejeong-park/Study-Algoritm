# 1012 유기농 배추

from collections import deque

t = int(input())
#   배추를 심은 배추밭 길이  배추의 위치 -> k

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if array[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

    return 1

result_list = []
while t>0:
    t-=1 # 두번 반복
    result = 0
    n, m, k =  map(int, input().split())
    array = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    # 배추가 심어진 위치
    for _ in range(k):
        x, y = map(int, input().split())
        array[x][y] = 1

    for i in range(n):
        for j in range(m):
            if array[i][j] == 1 and not visited[i][j]:
                result += bfs(i,j)
    result_list.append(result)


for answer in result_list:
    print(answer)