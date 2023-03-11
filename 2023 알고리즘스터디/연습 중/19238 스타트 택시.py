# 19238 스타트 택시
from collections import deque

n, m, fuel = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

x, y = map(int, input().split())
info = {}
for _ in range(m) :
	sx, sy, ex, ey = map(int, input().split())
	info[(sx-1, sy-1)] = (ex-1, ey-1)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_target(x, y, fuel) :
	visited = [[0] * n for _ in range(n)]

	# 택시와 승객이 같은 위치에 있을 때
	if array[x][y] == 2:
		return x, y, fuel
	# 같은 위치에 있지 않을 때
	else :
		min_distance = int(1e9)
		queue = deque([(x, y)])
		person_list = []
		while queue :
			x, y = queue.popleft()
			# 최단거리를 더 이상 구할 필요가 없는 경우
			if visited[x][y] > min_distance :
				break
			# start 안에 최단거리를 구할 리스트가 있는 경우
			if (x, y) in info.keys():
				min_distance = visited[x][y]
				person_list.append((x, y))

			for i in range(4):

				nx = x + dx[i]
				ny = y + dy[i]

				if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
					# 벽이 아니면
					if array[nx][ny] != 1 :
						visited[nx][ny] = visited[x][y] + 1
						queue.append((nx, ny))

		# 벽으로 막혀있어, 승객의 시작점을 찾지 못하는 경우
		if len(person_list) == 0:
			return -1, -1, -1
		else:
			person_list.sort()
			x, y = person_list[0][0], person_list[0][1]
			return x, y, visited[x][y]

def ride_the_taxi(sx, sy, ex, ey):
	visited = [[0] * n for _ in range(n)]
	queue = deque([(sx, sy)])

	while queue :
		x, y = queue.popleft()
		if x == ex and y == ey :
			break

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
				if array[nx][ny] != 1:
					visited[nx][ny] = visited[x][y] + 1
					queue.append((nx, ny))

	return x, y, visited[ex][ey]	# 도착

x, y = x-1, y-1
flag = False

for _ in range(m):

	start_x, start_y, target = find_target(x,y, fuel)
	if target < 0 :
		flag = True
		break
	fuel -= target
	end_x, end_y = info[(start_x, start_y)]
	target_x, target_y, min_distance = ride_the_taxi(start_x, start_y, end_x, end_y) 	# 택시 도착지점 (어차피 도착지점은 지정되어 있음)

	# 도착하지 못할 경우와 연료가 다 떨어진 경우
	if fuel - min_distance < 0 or (target_x, target_y) != (end_x, end_y):
		flag = True
		break

	# 값 갱신
	fuel += min_distance
	x, y = end_x, end_y
	del info[(start_x, start_y)]

if flag == True :
	print(-1)
else:
	print(fuel)