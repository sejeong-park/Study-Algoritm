# 8911 - 거북이

t = int(input())	# 케이스

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(t) :
	array = list(input())
	x, y, d, result = 0, 0, 0, 0
	max_x, max_y, min_x, min_y = 0, 0, 0, 0
	for control in array:
		# 좌우 방향 바꾸는 경우
		if control == 'R' :
			d = (d+1) % 4
		elif control == 'L' :
			d = (d-1) % 4
		elif control == 'F' :
			x += dx[d]
			y += dy[d]
		elif control == 'B' :
			x -= dx[d]
			y -= dy[d]

		max_x, max_y = max(max_x, x), max(max_y, y)
		min_x, min_y = min(min_x, x), min(min_y, y)

	result = abs(max_x - min_x) * abs(max_y - min_y)
	print(result)