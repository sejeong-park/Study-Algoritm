# 17142 - 연구소 3
from itertools import combinations
from collections import deque

n,m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

virus = []
wall = 0
for i in range(n):
    for j in range(n):
        if array[i][j] == 2:
            virus.append((i,j))
        if array[i][j] == 1:
            wall +=1


def bfs(active_virus, min_value):
    # time -> 시간 흐름과 방문 동시에 체크
    time = [[-1]*n for _ in range(n)]
    queue = deque([])

    for x,y in active_virus:
        queue.append((x,y))
        time[x][y] = 0 # 0초부터 시작

    max_value = 0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 내에 있고, 벽에 닿지 않으며, 방문하지 않은 것
            if 0<=nx<n and 0<=ny<n and array[nx][ny] != 1 and time[nx][ny] == -1:
                time[nx][ny] = time[x][y] + 1   # 시간 초 흐름
                queue.append((nx,ny))   # 벽이 아니면 큐에 넣기
                # 비활성 바이러스를 제외하고, time의 값 최대값 찾기
                if array[nx][ny] == 0:
                    max_value = max(max_value, time[nx][ny])

        # print(time)
        # 방문 안한 곳과 벽의 개수가 동일한지.
        wall_1 = list(sum(time, [])) # time
        if wall_1.count(-1) == wall:
            answer.append(max_value)
            min_value = min(max_value, min_value)

    return min_value

combination = combinations(virus, m)
answer = []
min_value = 1e9
for active_virus in combination:
    min_value = min(min_value, bfs(active_virus, min_value))

if min_value == 1e9:
    print(-1)
else:
    print(min_value)
