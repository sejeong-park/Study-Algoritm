# 14502 - 연구소
from itertools import combinations
from collections import deque
import copy
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

space, virus = [], []

for i in range(n):
	for j in range(m):
		if array[i][j] == 0:
			space.append((i,j))
		if array[i][j] == 2:
			virus.append((i,j))

space_to_wall = list(combinations(space, 3))	# 빈 공간을 3개로 넣을 공간

max_result = 0
# space_to_wall은 3개 테스트 케이스
for wall in space_to_wall :
	queue = deque(virus)
	area = copy.deepcopy(array)

	# 조합으로 공간을 벽으로 변환한다.
	for x, y in wall:
		area[x][y] = 1

	while queue:
		# 바이러스 퍼진다.
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 벽이 아니면,
			if 0<= nx < n and 0<= ny < m and area[nx][ny] == 0:
				area[nx][ny] = 2
				queue.append((nx, ny))

	safe_space = 0
	for i in range(n):
		for j in range(m):
			if area[i][j] == 0:
				safe_space += 1

	max_result = max(max_result, safe_space)

print(max_result)








