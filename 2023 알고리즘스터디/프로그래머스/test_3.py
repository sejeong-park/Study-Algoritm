boards_1 = [['00011', '01111', '21001', '11001', '01111'],
		  ['00011', '00011', '11111', '12101', '11111']]
boards_2 = [['1111', '1121', '1001', '1111'],
			['0000', '0000', '0000', '0002'],
			['0000', '0100', '0000', '0002'],
			['0000', '0010', '0121', '0010']]

from collections import deque

def bfs(x, y, board):
	visited = [[0] * len(board[0]) for _ in range(len(board))]
	queue = deque([(x,y)])
	cnt = 1
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]

	while queue :
		x, y = queue.popleft()
		case = 0
		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<len(board) and 0<= ny < len(board[0]):
				if board[nx][ny] == '1' and visited[nx][ny] == 0:
					queue.append((nx, ny))
					visited[nx][ny] = 1
					cnt += 1
					case += 1
		if case == 4:
			break
	if case == 4:
		return -1
	else:
		return cnt

def solution(boards) :
	answer = []

	for board in boards :
		size = 0
		for i in range(len(board)):
			for j in range(len(board[0])):
				if board[i][j] == '2':
					result = bfs(i, j, board)
				if board[i][j] != '0':
					size += 1
		if size == result :
			answer.append(1)
		else:
			answer.append(0)

	return answer

print(solution(boards_2))
