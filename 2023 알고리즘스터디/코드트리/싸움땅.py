# 싸움 땅

n, m, k = map(int, input().split())
location = [[0] * n for _ in range(n)]	# 플레이어의 위치
players = {}
points = [0] * (n+1)

array = []
for i in range(n):
	lists = list(map(int, input().split()))
	lines = []
	for j in range(n):
		if lists[j] != 0:
			lines.append([lists[j]])
		else:
			lines.append([])
	array.append(lines)

print(array)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(m):
	x, y, d, s = map(int, input().split())
	players[i+1] = [x-1, y-1, d, s, 0]
	location[x-1][y-1] = i+1

print(location)
print("초기값" , players)
print('-------------')
def get_gun(num):
	x, y, d, s, g = players[num]

	# 내가 총이 있다면
	if g != 0:
		array[x][y].append(g)

	array[x][y].sort(reverse = True)
	print(array[x][y], x, y)
	new_g = array[x][y].pop(0)

	players[num][-1] = new_g	# 무기 갱신해주기

def loser_move(num) :
	x, y, d, s, g = players[num]

	if g != 0 :
		array[x][y].append(g)

	nx = x + dx[d]
	ny = y + dy[d]

	# 만약 다른 사람이 있으면 90도 회전
	if location[nx][ny] != 0:
		nx = nx + dx[(d+1) % 4]
		ny = ny + dy[(d+1) % 4]

	# 이동 갱신
	players[num] = [nx, ny, d, s, 0]	# 총을 자리에 내려놔야 하기 때문
	location[nx][ny], location[x][y] = num, 0


def fight(now, target):
	print("fight")
	print("now : ",now,  players[now])
	print("target: ",target,  players[target])

	now_x, now_y, now_d, now_s, now_g = players[now]
	target_x, target_y, _, target_s, target_g = players[target]

	# 초기 능력치 여부여 따라 승패
	winner, loser = 0, 0
	if now_s + now_g < target_s + target_g:
		winner, loser = target, now
	elif now_s + now_g > target_s + target_g:
		winner, loser = now, target
	else:
		if now_s >= target_s :
			winner, loser = now, target
		else:
			winner, loser = target, now

	loser_move(loser)
	# winner의 위치 재정의
	players[winner] = [target_x, target_y, now_d, now_s, now_g]
	get_gun(winner)
	location[target_x][target_y], location[now_x][now_y] = winner, 0

	points[winner] += abs((target_g + target_s) - (now_g + now_s))



# 이동
def move(num) :
	x, y, d, s, g = players[num]

	nx = x + dx[d]
	ny = y + dy[d]

	# 격자를 벗어날 경우 정반대 방향으로 1만큼 가기
	if 0 <= nx < n and 0 <= ny < n:
		pass
	else:
		nx = x + dx[(d+2) % 4]
		ny = y + dy[(d+2) % 4]

	players[num] = [nx, ny, d, s, g]  # 이동에 대한 player 좌표 갱신

	# 이동지에 다른 플레이어가 있다면
	if location[nx][ny] != 0:
		fight(num, location[nx][ny])	# 싸우기
	# 없다면
	else:
		location[nx][ny], location[x][y] = num, 0 # 이동 체크
		get_gun(num) 	# 총 확인하기



# 라운드 반복
for _ in range(k):

	# 플레이어 위치 변경
	for i in range(m):
		move(i+1)	# player 번호 이동

		print(i+1, '-----------')
		print(players)
		print("location : ", location)
		print("gun : ", array)

	print(array)


print(points[1:])