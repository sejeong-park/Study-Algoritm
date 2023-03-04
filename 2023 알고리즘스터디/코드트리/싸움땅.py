n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

player = {}
points = [0] * (m + 1)
for i in range(m):
	x, y, d, s = map(int, input().split())
	array[x - 1][y - 1] = -(i + 1)  # 플레이어인지 판단 여부
	player[i + 1] = [x - 1, y - 1, d, s, 0]


def get_point(big, small):
	return big - small


def lose_user(num, x, y):
	_, _, direction, s, gun = player[num]
	# 총을 내려놓는다 -> 원래 있던것 보다 큰 거 내려놓기
	array[x][y] = max(gun, array[x][y])

	# 원래 방향대로 한칸이동
	nx = x + dx[direction]
	ny = y + dy[direction]
	# 만약 다른 플레이어가 있다면?
	if array[nx][ny] < 0:
		nx = x + dx[direction - 1 % 4]
		ny = y + dy[direction - 1 % 4]

	# player 위치 갱신
	player[num] = [nx, ny, (direction - 1) % 4, s, 0]


def win_user(num, x, y):
	_, _, d, s, gun = player[num]

	# 내가 들고 있는 무기와 땅에 있는 무기 비교
	if gun < array[x][y]:
		gun = array[x][y]  # 더 트다면 교체

	# player 위치 갱신
	player[num] = [x, y, d, s, gun]
	array[x][y] = -num  # 총 교체했으니까 번호로 반환


# player 끼리 싸울 경우
def fight(num, target_x, target_y):
	now_power = player[num][3] + player[num][4]  # 현재 플레이어의 힘

	target_num = -array[target_x][target_y]  # 상대 플레이어의 num
	target_power = player[target_num][3] + player[target_num][4]

	if now_power < target_power:
		points[target_num] = get_point(target_power, now_power)  # 점수 획득
		lose_user(num, target_x, target_y)
		win_user(target_num, target_x, target_y)

	elif now_power > target_power:
		points[num] = get_point(now_power, target_power)  # 점수 획득
		lose_user(target_num, target_x, target_y)
		win_user(num, target_x, target_y)

	# 만약 같을 경우
	else:
		# 초기 능력치 비교
		if player[num][3] < player[target_num][3]:
			lose_user(num, target_x, target_y)
			win_user(target_num, target_x, target_y)
		else:
			lose_user(target_num, target_x, target_y)
			win_user(num, target_x, target_y)

	return array

# 라운드 수
for _ in range(s):
	# 플레이어의 이동
	for i in range(m):
		x, y, d, s, gun = player[i + 1]

		nx = x + dx[d]
		ny = y + dy[d]

		# 0 <= nx < n and 0 <= ny < n
		# 격자를 벗어나는 경우 정반대 방향으로 1만큼 이동
		if n <= nx or nx < 0 or n <= ny or ny < 0:
			nx = x + dx[(d + 2) % 2]
			ny = y + dy[(d + 2) % 2]

		#########################
		# 만약 다음 블록에 총이 있는 경우
		if array[nx][ny] > 0:
			if gun == 0:
				gun = array[nx][ny]  # 무기 획득
			else:
				gun, array[nx][ny] = array[nx][ny], gun  # 무기 교체
			player[i+1][-1] = gun
		# 만약 다음 블록에 사람이 있는 경우
		elif array[nx][ny] < 0:
			array = fight(i + 1, nx, ny)

	print(player)

print(points)


