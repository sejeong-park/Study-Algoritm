import copy

m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
array = [[[] for _ in range(4)] for _ in range(4)]
fish_smell = [[0] * 4 for _ in range(4)]

shark_x, shark_y = map(int, input().split())
shark_x, shark_y = shark_x-1, shark_y-1

# array에 방향 넣기
for x, y, d in fish :
	array[x-1][y-1].append(d-1)

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

sx = [-1, 0, 1, 0]
sy = [0, -1, 0, 1]

def move_fish() :
	"""
	물고기 이동
	1. 상어가 있는 칸, 물고기 냄새 칸, 벗어나는 칸 X
	2. 45도 "반시계" 회전 후 이동. 이동 못하는 경우 그대로
	:return:
	"""

	new_array = [[[] for _ in range(4)] for _ in range(4)]
	for x in range(4) :
		for y in range(4) :
			for d in array[x][y] :
				for i in range(8) :
					fd = (d-i) % 8
					nx = x + dx[fd]
					ny = y + dy[fd]
					# 상어 있는 칸, 물고기 냄새칸, 벗어나는 칸이 아닌 것
					if (nx, ny) != (shark_x, shark_y) and (0 <= nx < 4 and 0 <= ny < 4) and fish_smell[nx][ny] == 0:
						new_array[nx][ny].append(fd) # 방향 추가
						break
				else :
					# for 문에서 결과를 찾지 못한다면
					new_array[x][y].append(d)
	return new_array

def shark_move(x, y, depth, cnt, visited):
	"""
	DFS
	상어는 3칸 이동
	1. 제외되는 물고기 수가 많고 > 이동방법 사전순 (백트래킹하면 자동으로 됨)
	2. 이동한 곳을 저장 > 물고기 냄새가 됨
	:param shark_x:
	:param shark_y:
	:return:
	"""
	global max_eat, eat, shark_x, shark_y
	if depth == 3:
		if max_eat < cnt :
			max_eat = cnt
			shark_x, shark_y = x, y
			eat = visited[:]
		return

	# 상어의 탐색
	for d in range(4) :
		nx = x + sx[d]
		ny = y + sy[d]

		if (0<= nx < 4 and 0 <= ny < 4):
			if (nx, ny) not in visited :
				visited.append((nx, ny))
				# cnt + temp[nx][ny] 물고기의 수 더해가기
				shark_move(nx, ny, depth + 1, cnt + len(temp[nx][ny]), visited) # dfs
				visited.pop() #왜 ?? 이걸 함??
			else :
				shark_move(nx, ny, depth + 1, cnt, visited) # dfs




for _ in range(s) :

	# temp 는 라운드 별! array 값

	# 1 . 모든 물고기 복제
	temp = copy.deepcopy(array)

	# 2. 물고기의 이동
	temp = move_fish()

	# 3. 상어의 이동
	max_eat, eat = -1, []
	shark_move(shark_x, shark_y, 0, 0, list())
	# 먹은 물고기들의 이동 -> 먹히고, 냄새 남기고
	for x, y in eat :
		if temp[x][y] :
			temp[x][y] = []
			fish_smell[x][y] = 3


	# 4. 냄새 사라짐 -> 라운드별로 2라운드 전에 냄새 하나씩 사라져
	for x in range(4) :
		for y in range(4) :
			if fish_smell[x][y] :
				fish_smell[x][y] -= 1

	# 5. 복제 마법
	for x in range(4) :
		for y in range(4) :
			array[x][y] += temp[x][y] # 원래 array에 연습하면서 이동했던 값들 붙여 넣기


# 물고기 수 구하기
answer = 0
for x in range(4) :
	for y in range(4) :
		answer += len(array[x][y])

print(answer)
