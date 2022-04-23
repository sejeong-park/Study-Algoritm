from collections import deque

n = int(input())
k = int(input())
data = [[0]*n for _ in range(n)]
turn_info = {}
for _ in range(k):
    a, b = map(int, input().split())
    data[a-1][b-1] = 1

l = int(input())
for _ in range(l):
    r, d = input().split()
    r = int(r)
    turn_info[r] = d
#######     입력 완료
# 동, 남, 서, 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,d):
    if d == 'L':
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

##### 시뮬레이션 시작
x,y, direction = 0,0,0
time = 1
data[x][y] = 2      # 뱀이라면 2로 변환

#### 뱀의 탐색 시작
queue = deque([(x,y)])
# 큐의 앞쪽은 뱀의 꼬리 / 큐의 뒤쪽은 뱀의 머리
while True:
    x = x + dx[direction]
    y = y + dy[direction]
    # 뱀이 잘 갔을 때
    if 0<= x < n and 0 <= y < n and data[x][y]!=2:
        # 뱀이 이동한 거리가 사과가 없으면
        if data[x][y] == 0:
            tx,ty = queue.popleft()
            data[tx][ty] = 0
        data[x][y] = 2
        queue.append((x,y))
        time += 1
        if time in turn_info.keys():
            direction = turn(direction, turn_info[time])
    else:
        break

print(time)