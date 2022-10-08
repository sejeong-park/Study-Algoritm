# 16234 - 인구이동
from collections import deque

n, l ,r = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    result
    queue = deque([(x,y)])
    visited[x][y] = True
    union = [(x,y)]     # 연합된 국가의 수
    count = array[x][y] # 현재 국가의 인구수
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵 범위 내에 있다면
            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                # 연합 조건에 맞다면
                if l<=abs(array[x][y] - array[nx][ny])<=r:
                    union.append((nx,ny))
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    count += array[nx][ny]

    # BFS 내에서 탐색 끝나면 각 연합의 국가의 인구수 별로 나누기
    for x, y  in union:
        array[x][y] = count//len(union)
    # 연합의 개수로 리턴
    return len(union)  # 만약 연합의 크기

result = 0
while True:
    visited = [[False]*n for _ in range(n)]
    case = []
    for i in range(n):
        for j in range(n):
            # 인구 연합을 맺지 않았다면
            if visited[i][j] == False:
                # 연합의 크기가 1보다 크면
                case.append(bfs(i,j))

    if len(case)==n*n:
        break
    result += 1

print(result)

