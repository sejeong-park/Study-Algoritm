# 19238 - 스타트 택
from collections import deque

n, m, feul = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split()) 	# 택시 위치

info = {}
for _ in range(m):
	sx, sy, ex, ey = map(int, input().split())
	info[(sx-1,sy-1)] = (ex-1, ey-1)
	array[sx-1][sy-1] = 2 # 승객 표시

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def find_target(x, y):

	visited = [[0] * n for _ in range(n)]
	queue = deque([(x, y)])

	while queue :
		x, y = queue.popleft()

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:

				if array[nx][ny] != 1 :
					visited[nx][ny] = visited[x][y] + 1
					queue.append((nx, ny))

	min_distance = int(1e9)
	target_x, target_y = -1, -1 # 최소 거리
	for point in info.keys():
		px, py = point
		min_distance = min(min_distance, visited[px][py])
		if min_distance == visited[px][py] :
			target_x = px
			target_y = py

	for i in range(n):
		for j in range(n) :
			print(visited[i][j], end = ' ')
		print()
	print('---------')

	return target_x, target_y, min_distance # 최소 거리 리턴

# DP로 해도 될 것 같다.
def start_to_end(x, y):

	visited = [[0]*n for _ in range(n)]
	queue = deque([(x, y)])

	while queue :
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n and visited[nx][ny] == 0:
				if array[nx][ny] != 1 :
					visited[nx][ny] = visited[x][y] + 1
					queue.append((nx, ny))

	for i in range(n):
		print(*visited[i])





# 실행 부분
x, y, min_distance = find_target(x-1, y-1) # 출발지에 있는 손님을 태우기 위한 거리
feul -= min_distance # 출발 이동 연료만큼 삭제




