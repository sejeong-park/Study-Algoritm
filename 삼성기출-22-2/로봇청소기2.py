from collections import deque

n, m = map(int, input().split())
x, y, d = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

# 북, 동, 남, 서
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 현재 위치를 청소
queue = deque([(x,y)])
visited[x][y] = 1
time = 1

while True:
	flag = 0
	for _ in range(4):	# 4방향 돌기
		d = (d+3)%4	# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 탐색
		nx = x + dx[d]
		ny = y + dy[d]
		# 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸 전진하고 1번 부터 진행
		if 0 <= nx < n and 0 <= ny < m and array[nx][ny] == 0 and visited[nx][ny] == 0:
			visited[nx][ny] = 1
			x, y = nx, ny
			time += 1
			flag = 1
			break

	# 네 방향 모두 청소가 되어 있거나, 벽인 경우에는 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 되돌아간다.
	if flag == 0:
		nx = x - dx[d]
		ny = y - dy[d]
		#
		if array[nx][ny] == 1:
			print(time)
			break
		else:
			x, y = x - dx[d], y - dy[d]