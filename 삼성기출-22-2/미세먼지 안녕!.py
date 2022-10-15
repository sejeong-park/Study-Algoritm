# 17144 - 미세먼지 안녕 !
from collections import deque

r, c, t = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(r)]
machine = []

for i in range(r):
	for j in range(c):
		if array[i][j] == -1:
			machine.append((i,j))



# 미세먼지 확산의 탐색
def dust(dust_table):
	spread_table = [[0]*c for _ in range(r)]

	dx = [-1,0,1,0]
	dy = [0,1,0,-1]

	# 먼지 휘날림의 배열
	dust_list = []
	for i in range(r):
		for j in range(c):
			if dust_table[i][j] > 0:
				dust_list.append((i,j))

	queue = deque(dust_list)
	while queue:
		x, y = queue.popleft()
		spread_list = []
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			# 범위 벗어나지 않고, 공기청정기가 없으면,
			if 0 <= nx < r and 0 <= ny < c and dust_table[nx][ny] != -1 :
				spread_list.append((nx,ny))

		# 퍼진 수와 퍼진 위치에 이동 수량 더하기
		spread_dust = dust_table[x][y] // 5
		for target in spread_list:
			spread_table[target[0]][target[1]] += spread_dust
		dust_table[x][y] = dust_table[x][y] - spread_dust * len(spread_list)	# 날린 거 빠져나간 리스ㅌ

	# 최종적으로 결과 더하기
	for i in range(r):
		for j in range(c):
			dust_table[i][j] += spread_table[i][j]

	return dust_table


def run(machine, dust_table):
	# 공기 청정기 위치
	up, down = machine
	# 위로 회전
	up_x, up_y = up
	for i in range(up_x):
		dust_table[up_x-i][up_y] = dust_table[up_x-i-1][up_y]
	for j in range(c-1):
		dust_table[0][j] = dust_table[0][j+1]
	for i in range(up_x):
		dust_table[i][c-1] = dust_table[i+1][c-1]
	for j in range(c-1):
		dust_table[up_x][(c-1)-j] = dust_table[up_x][(c-1)-j-1]
	dust_table[up_x][up_y] = -1
	# 아래로 회전
	down_x, down_y = down
	for i in range((r-1)-down_x):
		dust_table[(r-1)-down_x + i][down_y] = dust_table[(r-1)-down_x + i+1][down_y]
	for j in range(c-1):
		dust_table[r-1][j] = dust_table[r-1][j+1]
	for i in range((r-1)-down_x):
		dust_table[(r-1)-i][c-1] = dust_table[(r-1)-i-1][c-1]
	for j in range(c-1):
		dust_table[down_x][(c-1)-j] = dust_table[down_x][(c-1)-j-1]
	dust_table[down_x][down_y] = -1
	return dust_table


# t 초 후에 미세먼지의 양
for _ in range(t):
	array = dust(array)
	print(array)
	array = run(machine, array)
	print(array)
	print('----')


print(array)
total_result = 0
for i in range(r):
	for j in range(c):
		if array[i][j] > 0:
			print(array[i][j])
			total_result += array[i][j]

print(total_result)

