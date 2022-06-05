# 7579 - 토마토

import sys
from collections import deque

m,n,h = map(int, input().split())
array = []
queue = deque([])

for k in range(h):
    tmp = []
    # 한 박스의 그래프를 먼저 그리고, 다시 x를 탐색함으로써 큐에 넣어야 할 값을 반복 문 하나만으로 탐색해줌
    for i in range(n):
        tmp.append(list(map(int, sys.stdin.readline().split())))
        for j in range(m):
            if tmp[i][j] == 1:
                queue.append([k,i,j])
    array.append(tmp)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

while queue :
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0<=nx<h and 0<=ny<n and 0<=nz<m and array[nx][ny][nz] == 0:
            queue.append([nx,ny,nz])
            array[nx][ny][nz] = array[x][y][z] + 1
# print(array)
result = 0
for i in array:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        result = max(result, max(j))

print(result-1)