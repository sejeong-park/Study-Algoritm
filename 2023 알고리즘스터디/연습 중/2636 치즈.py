# 2636 치즈
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y , visited):
	queue = deque([(x,y)])
	visited[x][y] = 1
	lines = []
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
				if array[x][y] == 0 and array[nx][ny] == 1 and visited[nx][ny] != 2:
					lines.append((nx, ny))
					visited[nx][ny] = 2

				if array[nx][ny] == 0:
					queue.append((nx, ny))
					visited[nx][ny] = 1
	return lines

while True:
	visited = [[0] * m for _ in range(n)]
	lines = bfs(0,0,visited)
	if len(lines) == 0:
		break
	cheeze = len(lines)
	cnt += 1
	for point in lines:
		x, y = point
		array[x][y] = 0

print(cnt)
print(cheeze)
