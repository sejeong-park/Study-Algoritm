from collections import deque

from collections import deque


def solution(board):
	answer = 0
	n, m = len(board), len(board[0])
	for i in range(n):
		for j in range(m):
			if board[i][j] == "R":
				start_x, start_y = i, j

	# 상하 좌우
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	# BFS
	visited = [[int(1e9)] * m for _ in range(n)]
	queue = deque([(start_x, start_y, 0)])
	print(queue)
	while queue:
		x, y, cnt = queue.popleft()
		# 종료 조건
		if board[x][y] == 'G':
			break
		for i in range(4):
			# D 만나기 전까지 쭉이동 -> 몇칸 이동해야 하는지 모름 -> while
			nx, ny = x, y
			# 이동 조건
			while (0 <= nx + dx[i] < n) and (0 <= ny + dy[i] < m) and board[nx + dx[i]][ny + dy[i]] != 'D':
				nx += dx[i]
				ny += dy[i]
				print(nx, ny)

			# 이전에 도달한 경우보다, 현재 도달하는 경우가 더 적은 이동 횟수일 때 갱신
			if visited[nx][ny] > cnt + 1:
				visited[nx][ny] = cnt + 1
				queue.append((nx, ny, cnt + 1))

			print(visited)
			print(queue)

	return answer

board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
solution(board)