# 2573 - 빙산
from collections import deque
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def new_array(array):
    tmp_array = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if array[x][y] != 0:
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<m and array[nx][ny] == 0:
                        cnt+=1
                tmp_array[x][y] = array[x][y] - cnt
                if tmp_array[x][y] < 0 : tmp_array[x][y] = 0
    return tmp_array

def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny] and array[nx][ny]!=0:
                    visited[nx][ny] = True
                    queue.append((nx,ny))

result, flag = 0,0
tmp_break = [[0]*m for _ in range(n)]
while True:
    array = new_array(array)
    if array == tmp_break:
        flag = 1
        break
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and array[i][j] != 0:
                bfs(i,j)
                cnt+=1

    # 정답을 위함
    result+=1

    # 빙산의 단위를 멈추게 하기 위함
    if cnt>=2:
        break
if flag == 1:
    print(0)
else:
    print(result)