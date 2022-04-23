# 구슬 탈출 2

from collections import deque

n,m = map(int, input().split())
array = [list(map(input())) for _ in range(n)]
r_visited = [[False]*m for _ in range(n)]
b_visited = [[False]*m for _ in range(n)]

#   입력 받기
for i in range(n):
    for j in range(m):
        if array[i][j] == 'R':
            rx, ry = i,j
            r_visited[rx][ry] = True
        if array[i][j] == 'B':
            bx, by = i,j
            b_visited[bx][by] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def move(x, y, dx, dy):
    cnt = 0
    while True:
        if array[x+dx][y+dy] != '#' and array[x+dx][y+dy] != 'O':
            nx = x + dx
            ny = y + dy
            cnt+=1
        else:
            break
    return nx, ny, cnt

queue = deque([(rx,ry,bx,by,1)])

while queue:
    rx, ry , bx, by, count = queue.popleft()

    for i in range(4):
        rx, ry, r_move = move(rx,ry,dx[i],dy[i])
        bx, by, b_move = move(bx,by,dx[i],dy[i])

        n_rx = rx + dx[i]
        n_ry = ry + dy[i]

        n_bx = bx + dx[i]
        n_by = by + dy[i]

        if array[n_rx][n_ry] == 'O':
            if count < 10:
                print(count)
            else:
                print(-1)
            break
        if array[n_bx][n_by] == 'O':
            continue

        if n_