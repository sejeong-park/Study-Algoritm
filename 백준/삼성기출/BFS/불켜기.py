# 11967 불켜기
from collections import deque, defaultdict

n, m = map(int, input().split())

# x,y,a,b : (x,y)방에서 (a,b) 방의 불을 켜고 끌 수 있다는 의미 -> 한 방에 여러개 스위치
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for _ in range(n)]
light = [[False]*n for _ in range(n)]

turn_info = defaultdict(list)
for _ in range(m):
    x, y , a,b = map(int, input().split())
    turn_info[(x-1,y-1)].append((a-1,b-1))
result = 1 # 불을 켤 수 있는 방의개
def bfs(result):
    visited[0][0] = 1
    light[0][0] = 1
    queue = deque([(0,0)])
    while queue:
        x,y = queue.popleft()
        # 불을 킬 수 있는 곳
        for tx, ty in turn_info[(x,y)]:
            if not light[tx][ty]:
                light[tx][ty] = True # 새로 불켜기
                result += 1
                for i in range(4):
                    nx = tx + dx[i]
                    ny = ty + dy[i]

                    if 0<=nx<n and 0<=ny<n:
                        if visited[nx][ny]:
                            queue.append((nx,ny))

        # 현 위치를 기준으로
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<n and 0<=ny<n:
                if not visited[nx][ny] and light[nx][ny]:
                    queue.append((nx,ny))
                    visited[nx][ny] = 1

    return result


print(bfs(result))

