from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토가 들어 있지 않은 칸
# 익은 토마토와 인접해 있으면, 익은 토마토의 영향을 받아 익게 된다.
# 모두 익지 못하는 상황이면 -1을 출력
def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # x,y는 균일하게 들어왔으므로, 내부 n,m은 변하지 않음!!
            if 0<=nx<n and 0<=ny<m:
                if tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y]+ 1 # 익음 처리
                    queue.append((nx,ny))


queue = deque([])

####
for i in range(n):  # 행
    for j in range(m): # 열
        # BFS가 시작하는 시작점
        if tomato[i][j] == 1:
            queue.append((i,j))

bfs()
result = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    result = max(result, max(i))

print(result-1)




if 0 in tomato:
    print(-1)





"""
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1
"""





