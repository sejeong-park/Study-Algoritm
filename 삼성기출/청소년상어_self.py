# 19236 - 청소년 상어
from collections import deque
import copy
# 입력 배열 가공 -> 방향 키는 0부터 시작하므로!
array = [[] for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        fish.append([data[2*j], data[2*j+1]-1])
    array[i] = fish

for idx in array:
    print(idx)

# 방향 키
dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

## 물고기 먹기
result = 0

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    # 1을 더하면 왼쪽으로 회전되므로 !!
    return (direction + 1) % 8

def find_fish(array, index):
    # 인덱스 순서에 맞는 물고기 찾기
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)

    return None

def move_all_fished(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for idx in range(1, 17):
        # 물고기 번호에 맞는 위치 position
        position = find_fish(array, idx)
        # 포지션이 존재한다면
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]  # 방향
            # 해당 번호의 물고기 방향을 왼쪽으로 계속 회전시키면서 이동이 가능한지 확인
            for i in range(8):
                # 물고기는 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 범위 밖으로 벗어나지 않게
                if 0<=nx<4 and 0<=ny<4:
                    # 상어의 위치와 같지 않을 경우 순차적으로 물고기 교환
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction  # 현재 물고기에 45도 회전한 방향 넣어주기
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y] # 물고기들 자리 바꿔주기
                        break
                # 상어랑 마주치면, 방향을 왼쪽으로 이동
                direction = turn_left(direction)

# 상어가 현재 위치애서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    position = []
    direction = array[now_x][now_y][1] # 방향
    # 현재의 방향으로 게속 이동시키기
    for i in range(4):
        now_x = now_x + dx[direction]
        now_y = now_y + dy[direction]
        # 범위를 벗어나지 않는지 확인
        if 0<=now_x<4 and 0<=now_y <4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                position.append((now_x, now_y))
    return position

# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) # 리스트를 통째로 복사

    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1     # 물고기를 먹었으므로 번호 값을 -1로 반환

    move_all_fished(array, now_x, now_y)    # 전체 물고기 이동시키기

    # 상어가 이동할 차례이므로 상어의 이동가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최대값 저장
        return
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

# 청소년 상어의 시작 위치(0,0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)
