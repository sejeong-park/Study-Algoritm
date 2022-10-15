# 21609 상어중학교
from collections import deque
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 검은색 블록 -1
# 무지개 블록 0
# 일반  - 색상의 개수 (m의 케이스)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def block_group_list(x, y, color):
	queue = deque([(x,y)])
	rainbow, block_group = [],[]
	while queue:
		x, y = queue.popleft()
		if array[x][y] == 0:
			rainbow.append((x,y))
		block_group.append((x,y))
		visited[x][y] = 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# array를 벗어나지 않고, 방문하지 않을 경우
			if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
				#  color가 일정하거나 무지개색일 경우
				if array[nx][ny] == color or array[nx][ny] == 0:
					visited[nx][ny] = 1
					queue.append((nx,ny))
	# 무지개 색은 다른 것이 최대값일 수 있으니, visited 초기화
	for point in rainbow:
		visited[point[0]][point[1]] = 0

	return len(block_group), block_group, len(rainbow)


def distroy_max_group(max_groups):
	print(max_group)
	final_group = []	# 최종적인 그룹 넣기
	# max group이 1개일 때
	if len(max_groups) == 1:
		final_group = max_groups[0]

	else:
		max_rainbow = 0
		final_group = []
		for group in max_groups:
			rainbow = 0
			for x,y in group:
				if array[x][y] == 0:
					rainbow += 1

			max_rainbow = max(rainbow, max_rainbow)
			if max_rainbow == rainbow:
				final_group = group

	# 최대 그룹 array 초기화
	# 0은 무지개색이 있으므로 다른 값으로
	for line in final_group:
		x, y = line
		array[x][y] = ""

	return array

def gravity(array):
	# 바닥부터 카운트
	for j in range(n):
		empty = 0
		for i in range(n-1,-1,-1):
			if array[i][j] == "":
				empty += 1
			elif array[i][j] == -1:
				empty = 0
			else:
				if i+empty != i:
					array[i+empty][j] = array[i][j]
					array[i][j] = ""
	return array

def rotate_90(array):
	new_array = [ [0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			new_array[i][j] = array[j][(n-1)-i]
	return new_array

total_result = 0


while True:
	visited = [[0] * n for _ in range(n)]
	max_size = 0
	max_group = []
	max_rainbow = 0
	for i in range(n):
		for j in range(n):
			# 블록이 일반 블록일 경우 bfs 탐색
			if array[i][j] != 0 and array[i][j] != "" and array[i][j] != -1:
				size, block_group, rainbow = block_group_list(i,j, array[i][j])
				max_size = max(max_size, size)
				# 사이즈를 갱신하면 초기화
				if size >= max_size:
					max_rainbow = max(rainbow, max_rainbow)
					print(max_rainbow)
					# if rainbow > max_rainbow:
					# 	max_group = [block_group]
					max_group = [block_group]
	print(max_size, max_group)
	if max_size == 1:
		break

	distroy_max_group(max_group)
	total_result += max_size * max_size		# 점수 추가
	gravity(array)
	array = rotate_90(array)
	gravity(array)

print(total_result)


