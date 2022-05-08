# 그림 - BFS
from collections import deque

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]  # 방문 여부

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    # 한번 BFS 돌 때마다 최대 갯수 갱신
    value = 1
    visited[x][y] = True    # 초기값도 방문했으니까!
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx and nx < n and 0 <= ny and ny < m:
                if array[nx][ny] == 1 and visited[nx][ny] == False:
                    visited[nx][ny] = True      # "방문 했음"으로 갱신
                    value+=1
                    queue.append((nx,ny))
    return value

# x,y 초기화값과 picture 개수를 찾는 수
x,y,picture_cnt = 0,0,0
picture_size = []
# 부분 적으로 탐색
for i in range(n):
    for j in range(m):
        # 만약 그림으로 1이고, 방문하지 않았을 경우! -> BFS에 넣고 횟수 증가
        if array[i][j] == 1 and visited[i][j] == False:
            picture_cnt+=1
            #picture_size.append(bfs(i,j))       # 초기 시작 값은 i,j로 찾기 때문에 BFS를 시작할 값
            picture_size = max(picture_size, bfs(i,j))
print(picture_cnt)
print(picture_size)

