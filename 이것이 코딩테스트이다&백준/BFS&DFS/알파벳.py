from collections import deque
r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	queue = deque([(x,y,array[x][y])])
	while queue:
		x, y, alpha = queue.popleft()
		result = max(result, len(alpha))
		for idx in range(4):
			nx = x + dx[idx]
			ny = y + dy[idx]

			if 0<=nx<r and 0<=ny<c and array[nx][ny] not in alpha:
				queue.append((nx, ny, array[nx][ny] + alpha))
bfs(0,0)
print(result)

