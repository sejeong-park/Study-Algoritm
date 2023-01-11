# 백준 1913 - 달팽이

n = int(input())
k = int(input())
array = [[0]*n for _ in range(n)]

size = 1
# 가운데 좌표채우기
x = (n-1) // 2
y = (n-1) // 2
array[x][y] = 1
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 0
distance = 0
for idx in range(n*2-1):

	direction = idx%4 # 방향

	if direction == 0 or direction == 2 :
		if (idx+1) != n*2-1:
			distance += 1

	for _ in range(distance):
		nx = x + dx[direction]
		ny = y + dy[direction]
		# 마지막 출력값은 범위를 벗어나므로
		if 0<= nx < n and 0 <= ny < n:
			array[nx][ny] = array[x][y] + 1
		if array[nx][ny] == k:
			result_point = (nx +1, ny+1)
		x, y = nx, ny

for i in range(n):
	for j in range(n):
		print(array[i][j], end = ' ')
	print()
print(result_point[0], result_point[1])


