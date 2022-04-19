from collections import deque
INF = 1e9

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

now_x, now_y = 0,0
now_size = 2
ate = 0

fish_cnt = 0
fish_position = []

time = 0

# n의 공간 구하기
for i in range(n):
    for j in range(n):
        if 0 < array[i][j] <= 6 :   # 물고기의 개수와 위치 세기
            fish_cnt += 1
            fish_position.append((i,j))

        elif array[i][j] == 9:
            now_x, now_y = i,j # 아기 상어의 현재 위치 설정

array[now_x][now_y] = 0 # 아기상어 위치 초기화

dx = [-1,1,0,0]
dy = [0,0,-1,1]


# distance와 visited 구분해서 카운트
def bfs(now_x, now_y):
    # x, y, distance
    queue = deque([now_x, now_y, 0])
    # 방문한 것들 초기화에서 변환 시켜주는 부분
    visited = [[False]*n for _ in range(n)]
    visited[now_x][now_y] = True

    dist_list = []

    while queue:

        x, y, dist = queue.popleft()
        print(x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # (nx, ny)에 물고기가 있고, 아직 방문하지 않았다면
            if 0<=nx and nx<n and 0<=ny and ny<n and not visited[nx][ny]:
                # (nx, ny) 위치의 물고기가 아기상어보다 작거나 같다면
                if array[nx][ny] <= now_size:
                    visited[nx][ny] = True
                    # (nx, ny)위치의 물고기 크기가 아기상어보다 작다면
                    if 0< array[nx][ny] < now_size:
                        min_dist = dist # 최소 이동거리 갱신
                        dist_list.append((dist+1, nx, ny))  # 상어가 이동한 거리 및 위치 저장
                    if dist+1 <= min_dist:
                        queue.append((nx,ny,dist+1))

    if dist_list:
        # dist_list(distance, nx,ny)
        # dist_list[0]으로 상어가 이동한 총 거리 추출
        dist_list.sort()
        return dist_list[0]
    else:
        return False


while fish_cnt:
    result = bfs(now_x, now_y)
    print(result)
    if not result:
        break
    now_x, now_y = result[1], result[2]

    time += result[0]

    ate +=1
    fish_cnt -= 1
    if now_size == ate:
        now_size +=1
        ate = 0

    array[now_x][now_y] = 0

print(time)





