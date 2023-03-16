# 17143 낚시왕
import sys
"""
1. 낚시 왕이 왼쪽 -> 오른쪽 이동 (칸 이동은 1초)
	/낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어 잡음 -> 상어 사라짐/
	상어 이동
2. 상어의 이동
	겪자판의 경계를 넘는 경우 반대 방향으로 속력 유지 이동
3. 크기가 큰 상어가 나머지 상어 잡아먹는다
	상어는 한 칸에 여러 마리 있을 수 있다.
결과 : 잡은 상어의 크기의 합
"""
input = sys.stdin.readline
r, c, m = map(int, input().split())		# 상어의 수
array = [[0] * c for _ in range(r)]

for _ in range(m) :
	# 속력, 이동방향, 크기
	x, y, s, d, z = map(int, input().split())
	array[x-1][y-1] = (s, d-1, z)

# 위, 아래, 오른쪽, 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 낚시왕이 이동하면서 잡은 상어
def find_shark(person) :
	point = 0
	# 바다의 층수만 센다.
	for idx in range(r) :
		#  땅과 가장 가까운것만 센다. -> 한 줄 다 잡는 것이 아니라!
		if array[idx][person] != 0 :
			point += array[idx][person][-1] # 상어의 크기만큼 포인트에 추가
			array[idx][person] = 0 			# 낚시왕이 상어를 잡았으므로, 상어는 사라진다.
			break
	return point

def shark_move(array) :
	new_array = [[0] * c for _ in range(r)] 		# 새로운 상어판

	for x in range(r) :
		for y in range(c) :
			# 상어가 있다면
			if array[x][y] != 0 :
				# 상어 이동
				move_distance, direction, size = array[x][y]
				after_x, after_y = x, y
				# 속력만큼 이동
				while move_distance > 0 :
					after_x += dx[direction]
					after_y += dy[direction]
					# 상어가 겪자 밖에 나간다면 (근데, dx, dy값이 지정되어 있으므로 대칭을 해줘야 함)
					if (0 <= after_x < r and 0 <= after_y < c) :
						move_distance -= 1
					else:
						# 이동을 되돌리기
						after_x -= dx[direction]
						after_y -= dy[direction]
						# 만약 벗어나는 상어가가 상
						if direction == 0 :
							direction = 1
						elif direction == 1 :
							direction = 0
						elif direction == 2 :
							direction = 3
						elif direction == 3 :
							direction = 2
				# 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
				if new_array[after_x][after_y] == 0 :
					new_array[after_x][after_y] = (array[x][y][0], direction, size)
				else :
					if new_array[after_x][after_y][-1] < size :
						new_array[after_x][after_y] = (array[x][y][0], direction, size)
	return new_array

total_result = 0
for person in range(c) :
	# 낚시왕 = person
	total_result += find_shark(person)
	array = shark_move(array)


print(total_result)

