# 테스트 케이스는 맞는데, 오답으로 나옴 ..

from collections import deque
import copy

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

# 1. 아기상어의 위치 구하기
for i in range(n):
    for j in range(n) :
        if array[i][j] == 9:
            now_x, now_y = i, j         # 아기 상어의 위치
            array[now_x][now_y] = 0     # 아기 상어 공간 지워주기

now_size = 2

dx = [-1,0,1,0]
dy = [ 0,1,0,-1]

# 2. 지나갈 수 있는 거리에 대한 계산
def bfs(now_x, now_y) :
    queue = deque([(now_x, now_y)])
    distance = [[-1]*n for _ in range(n)]
    distance[now_x][now_y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n :
                # 조건 1 : 자기 자신보다 큰 물고기는 지나갈 수 없음 | 자기와 같은 크기 물고기는 지나갈 수 있음
                # 조건 2 : 방문하지 않은 거리를 탐색
                if array[nx][ny] <= now_size and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))

    return distance

# 먹을 물고기의 위치 찾기
def find(distance, now_size):
    # 물고기로부터의 거리 비교하기
    fish_position = dict()
    for i in range(n):
        for j in range(n):
            # 물고기 1 ~ 6까지인 크기 먹을 수 있는데, 현재의 상어 크기보다 작아야함
            if 1<= array[i][j] < now_size :
                # 거리, x, y
                if distance[i][j] not in fish_position:
                    fish_position[distance[i][j]] = []
                fish_position[distance[i][j]].append((i,j))

    # 딕셔너리가 없을 경우
    if len(fish_position) == 0:
        return None
    # 딕셔너리가 존재하는 경우 잡아먹을 물고기 구하기
    else:
        # 최단 거리
        distance = min(list(fish_position.keys()))
        return distance, fish_position[distance][0]


time = 0
ate = 0
# 아기상어가 먹을 거
while True:
    distance = bfs(now_x, now_y)    # 최단 거리 물고기 구하기
    fish_target = find(distance, now_size)    # 잡아먹을 물고기 거리와 위치
    # 잡아먹을 물고기가 없다면 종료
    if fish_target == None:
        print(time)
        break
    # 잡아먹을 물고기가 있다면
    else:
        distance, position = fish_target

        now_x, now_y = position # 물고기 위치 갱신
        array[now_x][now_y] = 0    # 물고기를 먹음

        ate += 1                # 물고기를 먹음

        if ate == now_size:     # 먹은 물고기와 아기상어의 크기가 일치하다면
            now_size += 1       # 상어의 크기 증가
            ate = 0             # 식사량은 초기화

        time += distance       # 거리 == 지나간 시간


