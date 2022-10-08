# 연구소 14502
import copy
from collections import deque
from itertools import combinations
n, m = map(int, input().split())
# array = [list(map(int, input().split())) for _ in range(n)]

array = []
space = []
virus = []
for i in range(n) :
	line = list(map(int, input().split()))
	array.append(line)
	for j in range(m):
		if array[i][j] == 0:
			space.append((i,j))
		if array[i][j] == 2:
			virus.append((i,j))

wall_block = list(combinations(space, 3))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
max_result = 0
for wall in wall_block:

	queue = deque(virus)
	array_copy = copy.deepcopy(array)
	safe_space = 0
	for x, y in wall:
		array_copy[x][y] = 1

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m and array_copy[nx][ny] == 0:
				array_copy[nx][ny] = 2
				queue.append((nx, ny))

	for i in range(n):
		for j in range(m):
			if array_copy[i][j] == 0:
				safe_space += 1

	max_result = max(max_result, safe_space)


print(max_result)







