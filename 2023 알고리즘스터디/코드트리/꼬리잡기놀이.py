# 꼬리잡기 놀이
from collections import deque

n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]	# 방문 확인
road = [[0] * n for _ in range(n)]
answer = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, num) :
	if array[x][y] in [2, 3]:
		group_person[num].append((x, y))
	visited[x][y] = True
	road[x][y] = num
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and array[nx][ny] != 0:
			if len(group_person[num]) == 1 and array[nx][ny] != 2:
				continue
			dfs(nx, ny, num)
group_person = {}
def init() :
	group_num = 0
	for x in range(n) :
		for y in range(n) :
			if array[x][y] == 1 :
				group_person[group_num+1] = deque([(x, y)])
				dfs(x, y, group_num+1)
				group_num += 1

	# print(group_person)

def move_first(num, first, second) :
	x, y = first
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n and road[nx][ny] == num and (nx, ny) != second :
			return (nx, ny)

def move_one() :

	for num in group_person.keys() :
		# 마지막 빼기
		first = group_person[num][0]	# 첫번째 애
		second = group_person[num][1]
		new_first = move_first(num, first, second)
		del group_person[num][-1] 		# 맨 마지막 사람 빼기
		group_person[num].appendleft(new_first) # 처음 사람 추가


def throw_the_ball(time) :
	global answer
	"""
	공이 던져지는 경우, 해당 선에 사람이 있으면, 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 된다.
	점수는 해당 사람이 머리사람을 시작으로 k 번째 사람이라면, k의 제곱만큼 점수를 얻게 된다.
	"""

	ball_point = [[0] * n for _ in range(n)]
	# 공을 몇번째 사람이 받는지 확인
	for num, value in group_person.items():
		for idx, point in enumerate(list(value)) :
			ball_point[point[0]][point[1]] = idx + 1

	# ball을 던지는 타이밍에 맞는 방향
	t = (time) % (4*n) + 1
	print(t)
	if t <= n :
		# 1 ~ n 라운드의 경우 왼쪽에서 오른쪽 방향으로 공을 던진다.
		for y in range(n) :
			if ball_point[t][y] != 0 :
				answer += (ball_point[t][y] * ball_point[t][y])
				return road[t][y]
	elif t<=2*n :
		# n+1 ~ 2n 라운드의 경우 아래에서 위로 방향으로 ㄱ오을 던진다.
		t-=n
		for x in range(n) :
			if ball_point[n-x][t] != 0:
				answer += (ball_point[n-x][t] * ball_point[n-x][t])
				return road[n-x][t]

	elif t<=3*n :
		t-= (2*n)
		for y in range(n) :
			if ball_point[n-t][n-y] != 0:
				answer += (ball_point[n-t][n-y] * ball_point[n-t][n-y])
				return road[n-t][n-y]

	else :
		t -= (3*n)
		for x in range(n) :
			if ball_point[x][n-t] != 0:
				answer += (ball_point[x][n-t] * ball_point[x][n-t])
				return road[x][n-t]

	return 0

init()
for time in range(k) :
	move_one()
	# print("move", group_person)
	ball_idx = throw_the_ball(time)
	# print("test" , ball_idx)
	# print(answer)
	if ball_idx == 0:
		continue
	group_person[ball_idx] = deque(reversed(group_person[ball_idx]))
	# print("rev", group_person)

print(answer)