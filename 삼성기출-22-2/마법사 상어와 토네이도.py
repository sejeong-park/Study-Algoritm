

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

# 방향별 모래 위치
left = [(1,1,0.01),(-1,1,0.01),(1,0,0.07),(-1,0,0.07),(1,-1,0.1),(-1,-1,0.1),(2,0,0.02),(-2,0,0.02),(0,-2,0.05),(0,-1,0)]
right = [(x,-y,z) for x,y,z in left]	# 반대로 뒤집기
down = [(-y,x,z) for x,y,z in left]
up = [(y,x,z) for x,y,z in left]

x, y = n//2, n//2
direction = {0:left, 1:down, 2:right, 3:up}
time = 0
answer = 0
def spread_sand(x,y,direction):
	global answer

	if y < 0:
		return

	total = 0
	for dx, dy, i in direction:
		nx = x + dx
		ny = y + dy
		# alpha값
		if i == 0 :
			next_sand = array[x][y] - total
		else:
			next_sand = int(array[x][y] * i)
			total += next_sand

		if 0<=nx<n and 0<= ny < n:
			array[nx][ny] += next_sand
		else:
			answer += next_sand


dx = [0,1,0,-1]
dy = [-1,0,1,0]
for i in range(2*n-1):
	d = i%4 # 방향
	if d == 0 or d == 2:
		time += 1
	for _ in range(time):
		nx = x + dx[d]
		ny = y + dy[d]
		spread_sand(nx, ny, direction[d])
		x, y, = nx, ny

print(answer)