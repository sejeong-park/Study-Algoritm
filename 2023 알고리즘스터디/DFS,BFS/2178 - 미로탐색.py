# 2178 - 미로 탐색
from collections import deque


n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

queue = deque([(0,0)])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:

	x, y = queue.popleft()

	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]

		if 0 <= nx < n and 0 <= ny < m and array[nx][ny] != 0:
			# 해당 노드를 처음 방문한 경우만
			if array[nx][ny] == 1:
				array[nx][ny] = array[x][y] + 1
				queue.append((nx, ny))


# print(array)
print(array[n-1][m-1])
