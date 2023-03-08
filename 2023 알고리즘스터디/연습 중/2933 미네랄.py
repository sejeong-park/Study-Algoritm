import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
array = [list(input()) for _ in range(r)]
n = int(input())
heights = list(map(int, input().split()))
Queue = deque()

def destroy(h, turn):
	x, y = h, 0
	if turn % 2 == 0:
		for idx in range(c) :
			if array[h][idx] == 'x' :
				array[h][idx] = '.'
				y = idx
				break

	else:
		for idx in range(c-1, -1, -1) :
			if array[h][idx] == 'x' :
				array[h][idx] = '.'
				y = idx
				break

	# 미네랄 파괴하고, 상하좌우를 살펴본다.
	for idx in range(4):
		nx = x + dx[idx]
		ny = y + dy[idx]
		if 0 <= nx < r and 0 <= ny < c :
			# 다른 미네랄이 있으면 클러스터 여부를 위해 queue 추가
			if array[nx][ny] == 'x' :
				Queue.append((nx, ny))

def bfs(x, y) :
	visited = [[0] * c for _ in range(r)]
	fall_list = []

	q = deque([(x, y)])
	visited[x][y] = 1

	while q :
		x, y = q.popleft()

		# 마지막 층이면,
		if x == r-1 :
			return
		if array[x+1][y] == '.' :	# 밑에가 빈칸이면
			fall_list.append([x, y])

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < r and 0 <= ny < c :
				if array[nx][ny] == 'x' and not visited[nx][ny] :
					visited[nx][ny] = 1
					q.append([nx, ny])

	fall(visited, fall_list)

def fall(visited, fall_list) :
	empty = 0
	k, flag = 1, 0
	while True :
		for x, y in fall_list :
			if x + k == r-1 :
				flag = 1
				break
			if array[x + k + 1][y] == 'x' and not visited[x + k + 1][y] :
				flag = 1
				break

		if flag :
			break
		k += 1

	for i in range(r-2, -1, -1) :
		for j in range(c) :
			if array[i][j] == 'x' and visited[i][j] :
				array[i][j] = '.'
				array[i+k][j] = 'x'




dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

turn = 0
for h in heights :
	h = r-h
	destroy(h, turn)

	while Queue :
		x, y = Queue.popleft()
		bfs(x, y)

	turn += 1

for i in range(r):
	for j in range(c) :
		print(array[i][j], end = '')
	print()