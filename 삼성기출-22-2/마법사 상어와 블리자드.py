# 21611번 - 마법사 상어와 블리자드
import copy
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
x, y = n // 2, n // 2
array[x][y] = -1

# 1,2,3,4 (direction 값은 -1 씩 해줘야 함)
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_result = {
	1 : 0,
	2 : 0,
	3 : 0
}

# 달팽이 구하는 방법 - 길 미리 저장
def make_road(array):
	seq_list = []
	# 좌 -> 하 -> 우 -> 상
	dr = [0, 1, 0, -1]
	dc = [-1, 0, 1, 0]
	size = 0
	r, c = x, y

	for idx in range(n * 2 - 1):
		direction = idx % 4  # 방향

		if direction == 0 or direction == 2:
			size += 1

		for _ in range(size):
			nr = r + dr[direction]
			nc = c + dc[direction]
			seq_list.append((r, c))
			r, c = nr, nc

	return seq_list

# 블리자드 마법 시행
def attack_to_direction(d, s):
	for i in range(1, s + 1):

		# 상하 값이면
		if d == 0 or d == 1:
			move_x = dx[d] * i
			move_y = dy[d]

		else:
			move_x = dx[d]
			move_y = dy[d] * i

		nx = x + move_x
		ny = y + move_y
		# 구슬 공백을 0으로 대체
		array[nx][ny] = 0

	return array

# 벽 파괴 시, 구슬의 이동 결과
def move_to_center():
	empty = 0
	# 반대로 뒤집는 stack
	road_rev = copy.deepcopy(road)
	road_rev.reverse()  # 스택 거꾸로 센다
	# 맨 마지막 스택 부터
	for index in range(len(road_rev) - 1, -1, -1):
		r, c = road_rev[index]
		if array[r][c] == 0:
			empty += 1
		else:
			if index + empty != index:
				# new는 더 앞에 있는 값
				new_r, new_c = road_rev[index + empty]
				array[new_r][new_c] = array[r][c]
				array[r][c] = 0

	return array

# 구슬의 폭발 - 투포인터
def distroy_marble():
	dupli = 0 # 중복 검사
	target = array[n//2][n//2]
	distroy_count = 1e9
	while distroy_count > 0:
		distroy_count = 0
		for start in range(len(road)):
			now_x, now_y = road[start] 	# 포인터
			# 중복일 경우 -> 중복인 칸만큼 카운트
			if array[now_x][now_y] == target and array[now_x][now_y] != 0:
				dupli += 1
			# 중복이 아닐 경우
			else:
				# 4개 이상 연속이였을 때
				if dupli >= 4 :
					distroy_count += 1
					# print("dupli : ", dupli)
					# 파괴해야할 묶음(개수)
					for idx in range(dupli):
						distroy_x, distroy_y = road[start-(idx+1)]
						total_result[array[distroy_x][distroy_y]] += 1
						# print(distroy_x, distroy_y, array[distroy_x][distroy_y])
						array[distroy_x][distroy_y] = 0

				# 다시 가던길 간다. dupli, target 초기화
				dupli = 1
				target = array[now_x][now_y]
				# print(f"x : {now_x}, y : {now_y} : target = {array[now_x][now_y]} :dupli : {dupli}")
		move_to_center()
	return array

# group 만들기
def make_group(x,y,target, index, visited):
	group = []
	for idx in range(index, len(road)):
		nx, ny = road[idx]
		if array[nx][ny] == target :
			visited[idx] = 1
			nx, ny = x, y
			group.append((nx, ny))
		else:
			break
	return len(group), target

# 새로운 array 만들기
def new_array():
	new_array = [[0]*n for _ in range(n)]
	target_road = [-1]
	visited = [0]*len(road)
	# 새로운 배열 만들기!!

	for index in range(1,len(road)):
		i, j = road[index]
		if array[i][j] != 0 and visited[index] == 0:
			len_group, marble_num = make_group(i,j, array[i][j], index, visited)
			target_road.append(len_group)
			target_road.append(marble_num)
			# print(len_group, marble_num)
	target_road = target_road + [0]*(len(road)-len(target_road))

	for index in range(len(road)):
		x, y = road[index]
		new_array[x][y] = target_road[index]

	return new_array

road = make_road(array)	# 정방형

for _ in range(m):
	distroy_cnt = 0
	d, s = map(int, input().split())
	attack_to_direction(d - 1, s)
	move_to_center()	# 구슬 가운데로 모으기
	distroy_marble()	# 구슬 4보다 큰 중복값 없을 때까지 반복
	array = new_array()

# print("final :: ", array)
answer = 0
for key, value in total_result.items():
	answer += key*value

print(answer)
