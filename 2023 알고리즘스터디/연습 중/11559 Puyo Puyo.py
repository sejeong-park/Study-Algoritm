# 11559 - Puyo Puyo
from collections import deque
array = [list(input()) for _ in range(12)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y):
	queue = deque([(x, y)])
	puyo_set = []
	while queue:
		x, y = queue.popleft()
		color = array[x][y]
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] :
				if array[nx][ny] == color:
					queue.append((nx, ny))
					visited[nx][ny] = True
					puyo_set.append((nx, ny))
	return puyo_set

def gravity(array):
	# 바닥부터 카운트
	for j in range(6):
		empty = 0
		for i in range(11, -1, -1):
			if array[i][j] == '.':
				empty += 1
			else:
				if i + empty != i:
					array[i + empty][j] = array[i][j]
					array[i][j] = '.'
	# for test in range(12):
	# 	print(*array[test])

answer = 0
while True:
	visited = [[False] * 6 for _ in range(12)]
	check = False
	for i in range(11,-1,-1):
		for j in range(6):
			if array[i][j] != '.' and not visited[i][j]:
				puyo_set = bfs(i,j)
				if len(puyo_set) >= 4:
					check = True
					for x, y in puyo_set:
						array[x][y] = '.'
	if not check :
		break
	gravity(array)
	answer += 1

print(answer)
