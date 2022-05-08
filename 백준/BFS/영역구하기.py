# 2583 - 영역 구하기
from collections import deque
n, m , k = map(int, input().split())
box = [[0]*m for _ in range(n)]
#print(box)
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1,x2):
        box[y1][i] = 1
        box[y2-1][i] = 1
    for i in range(y1,y2):
        box[i][x1] = 1
        box[i][x2-1] = 1

visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True
    box_size = 1
    while queue :
        x, y =queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and box[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
                box_size +=1

    return box_size

answer = []
### box 탐색
total_cnt = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0 and not visited[i][j]:
            box_size = bfs(i,j)
            answer.append(box_size)
            total_cnt +=1

answer.sort()
print(total_cnt)
print(' '.join(str(answer[i]) for i in range(len(answer))))
