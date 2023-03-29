import sys
import copy

input = sys.stdin.readline

n, m, h, k = map(int, input().split())

hiders = [[[] for _ in range(n)] for _ in range(n)]
tree = [[False] * n for _ in range(n)]

# 역방향 기준으로 현재 위치에서 술래가 움직여야 할 방향
seeker_next_dir = [[0] * n for _ in range(n)]
seeker_rev_dir = [[0] * n for _ in range(n)]

seeker_pos = (n//2, n//2)
forward_facing = True

answer = 0

# 도망자의 정보 입력
for _ in range(m) :
	x, y, d = map(int, input().split())
	hiders[x-1][y-1].append(d)
for _ in range(h) :
	x, y = map(int, input().split())
	tree[x-1][y-1] = True

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 정중앙으로부터 끝까지 움직이는 경로 계산
def initialize_seeker_path() :

	x, y = n//2, n//2
	direction, distance = 0, 1

	while x or y :
		for _ in range(distance) :
			seeker_next_dir[x][y] = direction
			x += dx[direction]
			y += dy[direction]
			seeker_rev_dir[x][y] = (direction+2)%4

			if not x and not y :
				break
		direction = (direction+1)%4
		if direction == 0 or direction == 2:
			distance += 1

def distance_from_seeker(x, y) :
	seeker_x, seeker_y = seeker_pos
	return abs(seeker_x - x) + abs(seeker_y- y)

def hider_move(x, y, direction, next_hiders) :

	nx = x + dx[direction]
	ny = y + dy[direction]

	# STEP 1. 만약 격자를 벗어난다면 방향을 틀어준다.
	if not (0<=nx<n and 0<=ny<n) :
		direction = (direction+2)%4
		nx = x + dx[direction]
		ny = y + dy[direction]
	# STEP 2. 그 다음 위치에 술래가 없다면 움직인다.
	if (nx, ny) != seeker_pos :
		next_hiders[nx][ny].append(direction)
	else :
		next_hiders[x][y].append(direction)

def hider_move_all() :
	# STEP 1. next_hider를 초기화
	next_hiders = [[[] for _ in range(n)] for _ in range(n)]

	# STEP 2. hider을 전부 움직여준다.
	for x in range(n) :
		for y in range(n) :
			# 술래와의 거리가 3이내인 도망자들만 움직여준다.
			if distance_from_seeker(x, y) <= 3:
				# 대상 방향 정보
				for direction in hiders[x][y] :
					hider_move(x, y, direction, next_hiders)
			# 그렇지 않다면 현재 위치 그대로 넣어준다.
			else:
				for direction in hiders[x][y] :
					next_hiders[x][y].append(direction)

	return next_hiders

def check_facing() :
	global forward_facing

	if seeker_pos == (0,0) and forward_facing :
		forward_facing = False

	if seeker_pos == (n//2, n//2) and not forward_facing :
		forward_facing = True

def seeker_direction(x, y) :
	direction = 0
	if forward_facing :
		direction = seeker_next_dir[x][y]
	else :
		direction = seeker_rev_dir[x][y]
	return direction

def seeker_move() :
	global seeker_pos

	x, y = seeker_pos
	direction = seeker_direction(x, y)


	# 술래를 한 칸 움직인다.
	nx = x + dx[direction]
	ny = y + dy[direction]
	seeker_pos = (nx, ny)

	# 술래가 끝에 도달했다면, 방향을 바꿔줘야 한다.
	check_facing()

def get_score(time) :
	global answer

	x, y = seeker_pos
	direction = seeker_direction(x, y)

	for distance in range(3) :
		nx = x + dx[direction] * distance
		ny = y + dy[direction] * distance
		if 0<=nx<n and 0<=ny<n and not tree[nx][ny] :
			# 해당 위치의 도망자 수만큼 점수를 얻는다.
			answer += time * len(hiders[nx][ny])
			#도망자 초기화
			hiders[nx][ny] = []


def simulation(time) :
	global hiders
	hiders = hider_move_all()	# hider 위치 이동
	seeker_move()				# 술래의 움직임
	get_score(time)

initialize_seeker_path()
for time in range(1, k+1) :
	simulation(time)

print(answer)

"""
5 3 1 1
2 4 1
1 4 2
4 2 1
2 4

"""