from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

def solution(maps):
	answer = 0

	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	queue = deque([(0, 0)])
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx <= len(maps)-1 and 0 <= ny <= len(maps[0])-1 and maps[nx][ny] == 1:
				maps[nx][ny] = maps[x][y] + 1
				queue.append((nx, ny))
	answer = maps[len(maps)-1][len(maps[0])-1]
	if answer == 1:
		return -1
	else:
		return answer

print(solution(maps))