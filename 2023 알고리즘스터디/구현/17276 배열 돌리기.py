# 17276 배열 돌리기
import copy
import sys

t = int(input())
total_array = []
for _ in range(t):

	n, degree = map(int, input().split())
	array = [list(map(int, input().split())) for _ in range(n)]
	time = (degree%360) // 45

	move_points = []
	move_points.append([(i, n//2) for i in range(n//2)])
	move_points.append([(i, n-1-i) for i in range(n//2)])
	move_points.append([(n//2 , n-1-i) for i in range(n//2)])
	move_points.append([(n-1-i, n-1-i) for i in range(n//2)])
	move_points.append([(n-1-i, n // 2) for i in range(n//2)])
	move_points.append([(n-1-i, i) for i in range(n//2)])
	move_points.append([(n//2, i) for i in range(n//2)])
	move_points.append([(i, i) for i in range(n//2)])

	change_points = copy.deepcopy(move_points)

	for index in range(8) :
		change_points[index] = move_points[(index + time)%8]


	new_array = copy.deepcopy(array)
	for before, after in zip(move_points, change_points):
		for i in range(n//2):
			x, y = before[i]
			nx, ny = after[i]
			new_array[nx][ny] = array[x][y]

	total_array.extend(new_array)

for i in range(len(total_array)):
	for j in range(n):
		print(total_array[i][j], end = ' ')
	print()