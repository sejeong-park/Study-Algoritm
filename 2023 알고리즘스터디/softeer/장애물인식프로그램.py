import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
	queue = deque([(x, y)])  # 큐 초기화
	cnt = 1	# 카운트 초기
	while queue:
		x, y = queue.popleft()
		visited[x][y] = True  # 방문 표시

		for i in range(4):
			# 다음 방문 확인
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n:
				# 0 이 아닐 경우에
				if array[nx][ny] != 0 and not visited[nx][ny]:
					cnt += 1
					queue.append((nx, ny))
					visited[nx][ny] = True
	return cnt

n = int(input())
array = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]


result = []
for i in range(n):
	for j in range(n):
		if array[i][j] == 1 and not visited[i][j]:
			result.append(bfs(i, j))

result.sort()
print(len(result))
for i in range(len(result)):
	print(result[i])