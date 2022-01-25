# BFS 대표 예제
from collections import deque

n,m = map(int,input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# BFS
def bfs(x,y):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복
    while queue:
        x,y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny]==0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1       # 1을 증가시켜줌으로 빠져나갈 경로에 1을 추가시켜 줌
                queue.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))