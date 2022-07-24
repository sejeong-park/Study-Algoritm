# 17144번 미세먼지 안녕!

r, c, t = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(r)]

# 상 하 좌 우
# [-1,1,0,0]
# [0,0,-1,1]
# 공기청정기는 항상 0번째 열에 있음

# 공기 청정기 위치 찾기
up, down = -1, -1
for i in range(r):
    if array[i][0] == -1:
        up = i
        down = i + 1

#   미세먼지 확산
# def spread():
#     # 상 좌 우 하
#     dx = [-1, 0, 0, 1]
#     dy = [0, -1, 1, 0]
#
#     tmp_array = [[0] * c for _ in range(r)]
#     for i in range(r):
#         for j in range(c):
#             if array[i][j] != 0 and array[i][j] != -1:
#                 tmp = 0
#                 for k in range(4):
#                     nx = dx[k] + i
#                     ny = dy[k] + j
#                     if 0<= nx < r and 0 <= ny < c and array[nx][ny] != -1:
#                         tmp_array[nx][ny] += array[i][j] // 5
#                         tmp = array[i][j] // 5
#                 array[i][j] -= tmp
#
#     for i in range(r):
#         for j in range(c):
#             array[i][j] += tmp_array[i][j]
def spread():
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    tmp_arr = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if array[i][j] != 0 and array[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < r and 0 <= ny < c and array[nx][ny] != -1:
                        tmp_arr[nx][ny] += array[i][j] // 5
                        tmp += array[i][j] // 5
                array[i][j] -= tmp

    for i in range(r):
        for j in range(c):
            array[i][j] += tmp_arr[i][j]
#   공기 청정기 위쪽 이동
# def air_up():
#     # 우 상 좌 하
#     dx = [0,-1,0,1]
#     dy = [1,0,-1,0]
#     x, y = up, 1
#     direct = 0
#     before = 0
#     while True:
#         nx = x + dx[direct]
#         ny = y + dy[direct]
#         if x == up and y == 0:
#             break
#         # 범위를 벗어나면 방향 회전
#         if nx < 0 or nx >= r or ny < 0 or ny >= c:
#             direct += 1
#         array[x][y], before = before, array[x][y]
#         x, y = nx, ny

def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        array[x][y], before = before, array[x][y]
        x = nx
        y = ny
#   공기 청정기 아래쪽으로 이동
def air_down():
    # 우 하 상 좌
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1 ,0]
    x, y = down, 1
    direct = 0
    before = 0
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            direct += 1
            continue
        array[x][y], before = before, array[x][y]
        x, y = nx, ny

for _ in range(t):
    spread()
    air_up()
    air_down()


result = 0
for i in range(r):
    for j in range(c):
        if array[i][j] > 0:
            result += array[i][j]

print(result)
