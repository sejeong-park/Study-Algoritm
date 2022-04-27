# 16236 - 아기 상어
from collections import deque
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#   아기 상어의 현재 위치와 현재 사이즈를 지정해줌
now_size = 2
fish_cnt = 0
fish_position = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x , now_y = i,j
        if 0 < array[i][j] <= 6:
            fish_position.append((i,j))
            fish_cnt +=1

# 거리를 구하는
def bfs(x,y):
    visited = [[False] * n for _ in range(n)]
    #print(visited)
    distance_list = []
    min_distance = int(1e9)

    queue = deque([(x,y, 0)])
    #print(queue)
    array[x][y] = 0
    visited[x][y] = True


    while queue:
        x,y, distance = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 현재 상어의 크기보다 작거나 같을 경우 -> 상어 먹어!
                if visited[nx][ny] <= now_size:
                    visited[nx][ny] = True
                    # 상어를 먹을 수 있다면
                    if 0<array[nx][ny]<now_size:
                        min_distance = distance
                        distance_list.append((distance+1, nx,ny))
                    if distance + 1 <= min_distance:
                        queue.append((nx, ny, distance +1))
    #print(queue)
    if distance_list:
        distance_list.sort()
        return distance_list[0]
    else:
        return False
time, eat_cnt = 0,0
while fish_cnt:
    #print(now_x,now_y)
    result = bfs(now_x,now_y)
    #print(result)
    if not result:
        break
    now_x, now_y = result[1], result[2]
    time += result[0]
    eat_cnt +=1
    fish_cnt -=1
    if now_size == eat_cnt:
        now_size +=1
        eat_cnt = 0
    array[now_x][now_y] = 0

print(time)



