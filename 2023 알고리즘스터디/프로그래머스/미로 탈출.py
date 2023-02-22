from collections import deque


def bfs(point, case, maps, visited):
	x, y = point
	queue = deque([(x, y)])

	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
				# 통로이고, 방문하지 않았을 때 증가
				if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
					queue.append((nx, ny))
					visited[nx][ny] += visited[x][y] + 1

					if maps[nx][ny] == case:
						return visited[nx][ny]
	return -1


def solution(maps):
	answer = 0
	start, end, lever = [], [], []
	visited = [[0] * len(maps[0]) for _ in range(len(maps))]
	for i in range(len(maps)):
		for j in range(len(maps[0])):
			if maps[i][j] == 'S':
				start = [i, j]
			elif maps[i][j] == 'E':
				end = [i, j]
			elif maps[i][j] == 'L':
				lever = [i, j]

	# find lever
	lever_time = bfs(start, 'L', maps, visited)
	if lever_time == -1:
		return -1
	else:
		visited = [[0] * len(maps[0]) for _ in range(len(maps))]
		visited[lever[0]][lever[1]] = lever_time

		end_time = bfs(lever, 'E', maps, visited)
		return end_time