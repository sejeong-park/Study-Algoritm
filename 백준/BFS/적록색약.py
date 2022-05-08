# 10026 - 적록색약
from collections import deque
n = int(input())
array = [list(map(str, input())) for _ in range(n)]

# 방문여부를 구분 지어야 함!! -> 왜 ? 케이스 자체가 다르니까!!
visited = [[False]*n for _ in range(n)]
visited_target = [[False]* n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y,color):
    queue = deque([(x,y,color)])
    visited[x][y] = True

    while queue:
        x, y, color = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                # 색이 일치하거나 방문 경험이 없으면
                # 색약이 아닌 사람!!
                if color == array[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny, array[nx][ny]))

same = ['R','G']
not_same = ['B']
def bfs_target(x, y, color):
    queue_target = deque([(x, y, color)])
    visited_target[x][y] = True

    color_list = same if color in same else not_same

    while queue_target:
        x, y, color = queue_target.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 색이 일치하거나 방문 경험이 없으면
                # 색약이 아닌 사람!!
                if array[nx][ny] in color_list and not visited_target[nx][ny]:
                    visited_target[nx][ny] = True
                    queue_target.append((nx, ny, array[nx][ny]))


cnt, target_cnt = 0,0
for i in range(n):
    for j in range(n):
        #
        # 방문하지 않은 경우만
        if visited[i][j] == False:
            bfs(i,j,array[i][j])
            cnt+=1
        if visited_target[i][j] == False:
            bfs_target(i,j,array[i][j])
            target_cnt+=1

print(cnt, target_cnt)
