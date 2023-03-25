import sys
from collections import deque


INT_MAX = sys.maxsize
EMPTY = (-1, -1)

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
# 편의점 목록 관리
target_list = []
for _ in range(m) :
	x, y = map(int, input().split())
	target_list.append((x-1, y-1))

person_list = [EMPTY] * m

time = 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visited = [[False] * n for _ in range(n)]
step = [[0] * n for _ in range(n)]

def bfs(start) :
	# 초기화
	visited = [[False] * n for _ in range(n)]
	step = [[0] * n for _ in range(n)]

	# 원소
	start_x, start_y = start
	queue = deque([(start_x, start_y)])
	visited[start_x][start_y] = True
	step[start_x][start_y] = 0


	while queue :
		x, y = queue.popleft()

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and array[nx][ny] != -1 :
				visited[nx][ny] = True
				step[nx][ny] = step[x][y] + 1
				queue.append((nx, ny))

	return step, visited


def simulation() :
	# STEP 1 : 격자에 있는 사람들에게 한하여, 편의점 방향을 향해 1칸 움직인다.
	for num in range(m) :
		# 아직 격자 밖에 있는 사람이거나, 이미 편의점에 도착한 사람이면 패스
		if person_list[num] == EMPTY or person_list[num] == target_list[num] :
			continue

		# 편의점 위치를 시작으로하는 BFS
		step, visited = bfs(target_list[num])		# visited, step 변경

		person_x, person_y = person_list[num] # 사람의 위치

		"""
		현재 위치에서 상좌우하 중 최단 거리 값이 가장 작은 곳을 고르면
		그 곳으로 이동하는 것이 최단거리 대로 이동하는 것이 된다.
		-> 그러한 위치 중 상좌우하 우선순위대로 가장 적절한 곳을 고른다.
		"""
		min_distance = INT_MAX
		min_x, min_y = -1, -1
		for i in range(4) :
			nx = person_x + dx[i]
			ny = person_y + dy[i]
			if 0<=nx<n and 0<=ny<n and visited[nx][ny] and min_distance > step[nx][ny] :
				min_distance = step[nx][ny]
				min_x, min_y = nx, ny

		# 우선순위가 높은 칸으로 이동한다.
		person_list[num] = (min_x, min_y)

		# 만약 편의점 위치와 같다면 불가능으로 바꿔줌
		if person_list[num] == target_list[num]	:
			person_x, person_y = person_list[num]
			array[person_x][person_y] = -1

	#  STEP 3 - 베이스 캠프 이동
	if time <=m :
		# 편의점을 시작으로 하는 베이스 캠프
		step, visited = bfs(target_list[time-1])	# 이 array를 기준으로 다시 찾기 !
		min_distance = INT_MAX
		min_x, min_y = -1, -1

		for x in range(n) :
			for y in range(n) :
				if visited[x][y] and array[x][y] == 1 and min_distance > step[x][y] :
					min_distance = step[x][y]
					min_x, min_y = x, y

		# 우선 순위가 가장 높은 베이스 캠프로 이동한다!
		person_list[time-1] = (min_x, min_y)
		# 해당 베이스 캠프로 이동하면, 앞으로 이동이 불가능하다.
		array[min_x][min_y] = -1

def end() :
	# 한사람이라도 편의점에 도착하지 못하면 -> 아직 끝나지 않음
	for num in range(m) :
		if person_list[num] != target_list[num] :
			return False
	return True

# 1분에 한 번 씩 시뮬레이션 진행
while True :
	time += 1
	simulation()
	if end() :
		break

print(time)