# 1913 달팽이

n = int(input())
k = int(input())
array = [[0]*n for _ in range(n)]

x = n // 2
y = n // 2
array[x][y] = 1

# 상 우 하 좌
dx = [-1,0,1,0]
dy = [0,1,0,-1]
distance = 0
direction = 0
result_point = (0,0)


for idx in range(n*2-1) :
	direction = (idx)%4

	if direction == 0 or direction == 2:
		distance += 1

	for _ in range(distance):
		nx = x + dx[direction]
		ny = y + dy[direction]
		array[nx][ny] = array[x][y] + 1
		if nx == 0 and ny == 0:
			break	# (0,0)에서 종료
		x , y = nx, ny

for i in range(n):
	for j in range(n) :
		if array[i][j] == k :
			result_point = (i,j)
		print(array[i][j] , end = ' ')
	print()

print(result_point[0] + 1, result_point[1] +1)