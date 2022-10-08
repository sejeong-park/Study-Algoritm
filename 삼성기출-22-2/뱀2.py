from collections import deque

n = int(input())
data = [[0]*n for _ in range(n)]
# 사과 좌표 위치
k = int(input())
for _ in range(k):
	x, y = map(int, input().split())
	data[x-1][y-1] = 1
l = int(input())
turn_info = dict()
for _ in range(l) :
	time, direction = input().split()
	turn_info[int(time)] = direction

def turn(direction, d):
	# (우) -> 상 -> 하 -> 좌 -> 상
	if d == 'L':
		direction = (direction-1)%4
	# (우) -> 하 -> 좌 -> 상 -> 우
	else:
		direction = (direction+1)%4

	return direction

# 우 상 좌 하
dx = [0,1,0,-1]
dy = [1,0,-1,0]

x, y, direction = 0,0,0
time = 1		# 시간 초
data[x][y] = 2

queue = dequ
e([(x,y)])	# 뱀

while True:
	x = x + dx[direction]
	y = y + dy[direction]

	if 0 <= x < n and 0<= y < n and data[x][y] != 2:
		# 사과를 먹지 않았다면
		if data[x][y] != 1:
			tail_x, tail_y = queue.popleft()
			data[tail_x][tail_y] = 0

		data[x][y] = 2 	# 사과를 먹고
		queue.append((x,y))	# 뱀의 길이가 길어진다.

		if time in turn_info.keys():
			direction = turn(direction, turn_info[time])
		time += 1
	else:
		break
print(time)

