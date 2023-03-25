# 코드트리 빵
import sys
from collections import deque
import copy


n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]	# 베이스 캠프 지정된 곳


# 현재 사람들의 좌표 저장
person_position = {}

target_position = {}
for num in range(m) :
	x, y = map(int, input().split())
	target_position[num+1] = [x-1, y-1]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def find_min_distance(num) :
	"""
	최단 거리
		- 상하좌우 인접한 칸 중 이동가능한 칸으로만 이동하여, 도달하기까지 거쳐야하는 칸의 수
	"""
	""""사람의 현재 위치로부터, 편의점 까지의 최단거리 경로"""
	person_x, person_y = person_position[num]
	target_x, target_y = target_position[num]

	direction_list = []
	min_distance = int(1e9)
	"""시간 초과 우려"""
	for d in range(4) :
		direction_x = person_x + dx[d]
		direction_y = person_y + dy[d]

		if not (0<=direction_x<n and 0<=direction_y<n) :
			continue
		if array[direction_x][direction_y] == -1 :
			continue

		# 방향에 대한 queue 초기화
		queue = deque([(direction_x, direction_y)])
		distance = [[0] * n for _ in range(n)] # direction 기준

		while queue :
			x, y = queue.popleft()
			if (x, y) == (target_x, target_y) :
				direction_list.append((distance[target_x][target_y], d))
				break
			for i in range(4) :
				nx = x + dx[i]
				ny = y + dy[i]
				if 0<=nx<n and 0<=ny<n and array[nx][ny] != -1 and distance[nx][ny] == 0:
					queue.append((nx, ny))
					distance[nx][ny] = distance[x][y] + 1

	# print(direction_list)
	if direction_list :
		direction_list.sort()
		direction = direction_list[0][1]
		update_x = person_x + dx[direction]
		update_y = person_y + dy[direction]


	return update_x, update_y

def find_basecamp(num) :
	"""
	조건 3.
		- t<=m
		- t번 사람은 자신이 가고 싶은 편의점과 가장 가까이 있는 베이스 캠프에 들억나다.
		- 가장 가까이 있는 베이스 캠프 -> 최단거리에 해당하는 곳
		- 가까운 베이스 캠프가 여러개라면 ? -> 행 - 열 순서
		- t 번 사람이 베이스 캠프로 이동하는 데는 시간이 전혀 소요되지 않음
		- 이 때 부터 다른 사람들은 해당 베이스캠프가 잇는 칸을 지나갈 수 없음
	"""
	distance = [[0] * n for _ in range(n)]
	target_x, target_y = target_position[num]	# 편의점의 위치

	queue = deque([(target_x, target_y)])
	basecamp = []
	min_distance = int(1e9)

	while queue :
		x, y = queue.popleft()
		if array[x][y] == 1 :
			if min_distance == distance[x][y] :
				basecamp.append((x, y))
			if min_distance < distance[x][y] :
				break
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n and distance[nx][ny] == 0 and array[nx][ny] != -1:
				queue.append((nx, ny))
				distance[nx][ny] = distance[x][y] + 1
				# 베이스 캠프를 만나면, 종료
				if array[nx][ny] == 1 :
					min_distance = min(min_distance, distance[nx][ny])

	# 베이스캠프 찾기
	if basecamp :
		basecamp.sort()
		person_x, person_y = basecamp[0][0], basecamp[0][1]
		person_position[num] = [person_x, person_y]
		array[person_x][person_y] = -1 		# 베이스캠프에 위치가 정해지면 더 넘어오지 못하도록 한다.


def simulation(num) :
	# "조건 1과 조건 2가 실행될 경우"

	"""
	조건 1.
		- 격자에 있는 사람들이 본인이 가고 싶은 편의점 방향을 향해 1칸 이동
		- 최단거리 움직이는 방법 여러개 -> 우선순위에 따라 이동
	"""
	nx, ny = find_min_distance(num)
	person_position[num] = [nx,ny]	# 새로 이동한 번호 넣기

	"""
	조건 2.
		- 편의점에 도착한다면 해당 편의점에서 멈춤
		- 이 때부터 다른 사람들은 해당 편의점이 있는 칸을 지날 수 없음
	"""
	if [nx, ny] == target_position[num] :
		del person_position[num]
		array[nx][ny] = -1
		check[num-1] = True

"""
5 3
0 0 0 0 0
1 0 0 0 1
0 0 0 0 0
0 1 0 0 0
0 0 0 0 1
2 3
4 4
5 1

"""


time = 1
check = [False] * m
while True :
	# 테스트
	if check.count(True) == m:
		break
	# person의 움직임 -> person이 격자 내에 있을 때,
	for num in range(m):
		if num+1 in person_position.keys() :
			simulation(num+1)
	if time <= m :
		# time과 person_num이 일치할 경우
		find_basecamp(time)		# 최단거리의 basecamp 찾기
	# print(person_position)
	time += 1

"""
결과값 -> 총 몇 분 후에 모두 편의점에 도착하는 지
"""
print(time-1)