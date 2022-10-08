# 20057 - 마법사 상어와 토네이

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


# 방향별 바뀌는 모래의 위치
left = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
         (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x,y,z in left]
down = [(-y, x, z) for x,y,z in left]
up = [(y, x, z) for x,y,z in left]

# 모래 계산하는 함수
def sand_wind(x, y, direction):
    global result
    if y<0:
        return

    total = 0 # alpha
    for dx, dy, score in direction:
        nx = x + dx
        ny = y + dy

        # alpha값을 나타내는 0이면
        # total은 다른 array에서 이미 뺀 값들이 있으므로, 처음 모래가 시작한 값에서 뺀애들의 나머지 값
        if score == 0:
            new_sand = array[x][y] - total
        # alpha가 아닌 값들인데, 알파가 아닌 값에 적용된 비율만큼 total에 넣어줌
        else:
            new_sand = int(array[x][y]*score)
            total += new_sand


        if 0<=nx<n and 0<=ny<n:
            array[nx][ny] += new_sand
        else:
            result += new_sand


# 토네이도의 회전 방향별 위치
dict = {0: left, 1: down, 2: right, 3:up}

dx = [0,1,0,-1]
dy = [-1,0,1,0]

x, y = n//2, n//2
distance, result = 0, 0
# 토네이도의 회전 수
for i in range(2*n-1):
    direction = i % 4
    if direction == 0 or direction == 2:
        distance += 1

    for _ in range(distance):
        nx = x + dx[direction]
        ny = y + dy[direction]
        sand_wind(nx,ny, dict[direction])
        x, y = nx, ny




