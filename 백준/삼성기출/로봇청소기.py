# 14503 - 로봇 청소기
from collections import deque
n,m = map(int, input().split())
x,y,direction = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

# 시작 방향의 위치 북 0, 동 1, 남 2, 서 3
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left(direction):
    direction -=1
    # 방향이 내부로 들어가면
    if direction == -1:
        direction = 3

# 초기화
visited[x][y] = True
cnt = 0
turn_time = 0
while True:
    turn_left()

    nx = x + dx[direction]
    ny = y + dy[direction]

    if visited[nx][ny] == False and array[nx][ny] == 0:
        # 회전 완료
        visited[nx][ny] = True
        x, y = nx, ny
        cnt+=1
        # 전진 했을 때 턴타임 리셋
        turn_time = 0  # 다음으로 넘어갈 때 턴타임 리셋
    else:
        turn_time +=1    # 한번 더 턴

    # 네 방향 다 돌았을 때
    if turn_time == 4:
        print('메롱')


turn_left(3)
