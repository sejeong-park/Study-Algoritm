from collections import deque

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 지훈이 탐색
queue_j = deque([])
visited_j = [[0]*m for _ in range(n)]
# 불의 탐색
queue_f = deque([])
visited_f = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if array[i][j] == 'J':
            queue_j.append((i,j))
            # 지훈이가 방문하면 visited 체크해주기
            visited_j[i][j] = 1
        elif array[i][j] == 'F':
            queue_f.append((i,j))
            # 불이 방문하면 visited 체크해주기
            visited_f[i][j] = 1

# 불먼저 계산하고, 지훈이 탈출구 계산함
def bfs():
    # 불의 탐색
    while queue_f:
        x, y = queue_f.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                # 방문하지 않고, 벽이 아닐 경우에 탐색
                if visited_f[nx][ny]==0 and array[nx][ny] != '#':
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    queue_f.append((nx,ny))

    # 지훈이의 탐색
    while queue_j:
        x, y = queue_j.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if array[nx][ny] != '#' and visited_j[nx][ny] == 0:
                    # 불이 방문하지 않았거나, 불이 도달하는 시간보다 더 짧은 시간안에 지훈이 도달할 수 있다면 !!!
                    if visited_f[nx][ny] == 0 or visited_f[nx][ny] >  visited_j[x][y] +1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        queue_j.append((nx,ny))
                    else:
                        # 아닐 경우 jihoon 0으로 리턴
                        return visited_j[x][y]

    return "IMPOSSIBLE"

print(bfs())