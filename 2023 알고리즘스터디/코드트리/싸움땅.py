# 싸움땅 : 2022년 하반기 오전 1번 문제
import sys

"""
총의 공격력, 플레이어의 초기 능력치, 플레이어의 번호
1. 플레이어의 이동
- 첫번째 플레이어부터 순차적으로 본인이 향하고 잇는 방향대로 한칸만큼 이동
	- 해당 방향으로 나갈 때 격자를 벗어나는 경우 정반대 방향으로 바꾸어서 1만큼 이동
case1 : 이동한 방향에 플레이어가 없다면, 해당 칸에 총이 있는지 확인
	- 만약 총이 있는 경우, 해당 플레이어는 총 획득
	- 플레이어가 총을 이미 가지고 있는 경우, 공격력이 더 쎈 총 획득, 총을 해당 격자에 놓는다.
case2 : 이동한 방향에 플레이어가 있는 경우
	- 두 플레이어가 싸운다.
	- 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합 비교 -> 더 큰 플레이어 승
	- 능력치가 같은 경우, 초기 능력치가 높은 플레이어 승
	- POINT : 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이

2. 진 플레이어
- 자신이 가지고 있는 총을, 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한칸 이동
	- 만약 이동하려는 칸에 다른 플레이어가 있거나, 격자 범위 밖인 경우, 오른쪽으로 90도 회전 / 빈칸이 보이는 순간 이동
	- 만약 해당 칸에 총이 있다면 해당 플레이어는 가장 공격력이 높은 총을 획득 / 나머지 총을 바닥에 놓는다.

3. 이긴 플레이어
- 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득
- 나머지 총 격자에 내려 놓음
"""

n, m, k = map(int, input().split())
array = [[] * n for _ in range(n)]
for x in range(n):
	line = list(map(int, input().split()))
	for y in range(n):
		if line[y] == 0:
			gun = []
		else:
			gun = [line[y]]
		array[x].append([0, gun])

player = {}
for num in range(m):
	x, y, d, s = map(int, input().split())
	player[num + 1] = [x - 1, y - 1, d, s, 0]  # 총까지
	array[x - 1][y - 1][0] = num + 1  # number 적어주기

# print(array)
# print(player)
# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def get_gun(x, y, g):
	# 자신의 총의 값을 준다.
	if g != 0:
		array[x][y][1].append(g)

	max_gun = max(array[x][y][1])
	array[x][y][1].remove(max_gun)  # 가져갈 최대값 gun을 뺀다

	return max_gun


def loser_move(num):
	"""
	진 사람의 이동
	- 자신이 가지고 있는 총을, 해당 격자에 내려놓고, 해당 플레이어가 원래 가지고 있던 방향대로 한칸 이동
		- 만약 이동하려는 칸에 다른 플레이어가 있거나, 격자 범위 밖인 경우, 오른쪽으로 90도 회전 / 빈칸이 보이는 순간 이동
		- 만약 해당 칸에 총이 있다면 해당 플레이어는 가장 공격력이 높은 총을 획득 / 나머지 총을 바닥에 놓는다.
	"""
	x, y, d, s, g = player[num]

	# 1. 자신이 가지고 있던 총을 해당 격자에 내려놓는다.
	if g != 0:
		array[x][y][1].append(g)  # 총 해당 격자에 내려 놓는다.
	g = 0

	# 2. 원래 가지고 있던 방향대로 한 칸 이동
	for i in range(4):
		nd = (d + i) % 4
		nx = x + dx[nd]
		ny = y + dy[nd]
		# 범위에 해당하는 칸을 찾으면 바로 종료
		if 0 <= nx < n and 0 <= ny < n and array[nx][ny][0] == 0:
			break

	# 3. 만약 이동할 칸에 총이 있다면 공격력이 가장 높은 총을 줍닌다.
	if len(array[nx][ny][1]) != 0:
		g = get_gun(nx, ny, g)

	# 4. 플레이어 위치 갱신
	player[num] = [nx, ny, nd, s, g]
	array[nx][ny][0] = num


def winner_move(num):
	"""
	3. 이긴 플레이어
	- 승리한 칸에 떨어져 있는 총들과 원래 들고 있던 총 중 가장 공격력이 높은 총을 획득
	- 나머지 총 격자에 내려 놓음
	"""
	x, y, d, s, g = player[num]
	array[x][y][0] = num  # 영역표시
	if len(array[x][y][1]) != 0:
		g = get_gun(x, y, g)
	player[num] = [x, y, d, s, g]


def player_move(num):
	x, y, d, s, g = player[num]
	array[x][y][0] = 0  # 현재 위치의 플레이어 초기화

	# 플레이어의 이동
	nx = x + dx[d]
	ny = y + dy[d]
	if not (0 <= nx < n and 0 <= ny < n):
		d = (d + 2) % 4
		nx = x + dx[d]
		ny = y + dy[d]

	# 플레이어의 현재 위치를 표시
	player[num] = [nx, ny, d, s, g]

	# 이동한 방향에 플레이어가 없다면
	if array[nx][ny][0] == 0:
		if len(array[nx][ny][1]) != 0:
			g = get_gun(nx, ny, g)
		player[num] = [nx, ny, d, s, g]  # gun값 갱신
		array[nx][ny][0] = num  # array의 위치값 갱신

	# 이동한 방향에 플레이어가 있다면
	else:
		winner, loser = fight(num, array[nx][ny][0])  # 이동할 방향의 대상과 싸우기
		# print("win : ", winner , "lose : ", loser)
		loser_move(loser)
		winner_move(winner)


def fight(a_player, b_player):
	"""
	case2 : 이동한 방향에 플레이어가 있는 경우
	- 두 플레이어가 싸운다.
	- 해당 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합 비교 -> 더 큰 플레이어 승
	- 능력치가 같은 경우, 초기 능력치가 높은 플레이어 승
	- POINT : 각 플레이어의 초기 능력치와 가지고 있는 총의 공격력의 합의 차이
	"""
	_, _, _, a_s, a_g = player[a_player]
	_, _, _, b_s, b_g = player[b_player]

	winner, loser = 0, 0
	# 능력치가 같은 경우
	if (a_s + a_g) == (b_s + b_g):
		if a_s > b_s:
			winner = a_player
			loser = b_player
		else:
			winner = b_player
			loser = a_player
	elif (a_s + a_g) > (b_s + b_g):
		winner = a_player
		loser = b_player
	else:
		winner = b_player
		loser = a_player

	# 이겼을 경우 포인트 적립
	points[winner] += (player[winner][3] + player[winner][4]) - (player[loser][3] + player[loser][4])

	return winner, loser


points = [0 for _ in range(m + 1)]
for _ in range(k):  # 라운드 회전 시키기
	# 플레이어의 이동
	for num in range(m):
		# print(num+1)
		player_move(num + 1)
# for i in range(n) :
# 	print(*array[i])
# print(player)
# print()

print(*points[1:])