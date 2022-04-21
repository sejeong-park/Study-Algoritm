from collections import deque
import copy
n, m = map(int, input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    # 바이러스 인 경우, queue에 바이러스 위치 추가
    for i in range(n):
        for j in range(m):
            # 바이러스 이면
            if tmp_graph[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx and nx < n and 0 <=ny and ny < m:
                # 안전영역이면!
                if tmp_graph[nx][ny] == 0:
                    # 바이러스로 퍼트림
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    cnt = 0

    for i in range(n):
        # 0 (안전영역인 개수 세기)
        cnt += tmp_graph[i].count(0)

    answer = max(answer, cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0
makeWall(0)
print(answer)
