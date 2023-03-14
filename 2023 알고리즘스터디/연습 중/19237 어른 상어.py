import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
# 0은 빈칸, x번 상어가 있는 칸
array = [list(map(int, input().split())) for _ in range(n)]
smell = [[[0,0]] * n for _ in range(n)] # 냄새를 세는 array

# 상어의 냄새 위치 초기화
for i in range(n) :
	for j in range(n) :
		if array[i][j] != 0 :
			smell[i][j] = [array[i][j] , k]

direction = list(map(int, input().split()))		# m마리의 방향
direction = [i-1 for i in direction] 			# 방향 index 맞추기

# 1 : 상 / 2 : 하 / 3 : 왼 / 4 : 오
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 우선순위
order = {}
for num in range(m) :
	order[num+1] = {}
	# 상하좌우 순서
	for i in range(4) :
		line = list(map(int, input().split()))
		order[num+1][i] = [i-1 for i in line]

def shark_move(x, y) :
	shark_num = array[x][y]
	shark_direct = direction[shark_num-1] # shark번호는 index + 1
	shark_direct_order = order[shark_num][shark_direct]  # # 상어의 이동방향 우선순위
	# print(shark_num, shark_direct, shark_direct_order)

	# 1. 인접한 칸 중 아무 냄새가 없는 칸의 방향
	found = False			# 냄새가 나는 것이 있다면
	for d in shark_direct_order :
		nx = x + dx[d]
		ny = y + dy[d]
		if 0 <= nx < n and 0 <= ny < n :
			if smell[nx][ny][1] == 0 :
				direction[shark_num-1] = d 		# shark 방향 업데이트
				# 상어 이동 시키기 -> 더 작은 것이 유리함
				if new_array[nx][ny] == 0:
					new_array[nx][ny] = shark_num
				else :
					new_array[nx][ny] = min(new_array[nx][ny] , shark_num)
				found = True
				break
	# 변경될 대상 업데이트 하지 못했으면, 자신의 냄새 내에서 찾는다.
	if not found :
		for d in shark_direct_order :
			nx = x + dx[d]
			ny = y + dy[d]
			if 0 <= nx < n and 0 <= ny < n :
				# 자신과 같은 냄새가 나면,
				if smell[nx][ny][0] == shark_num :
					direction[shark_num-1] = d
					new_array[nx][ny] = shark_num
					break

	# print(shark_num , x, y, nx, ny)

def update_smell() :
	for x in range(n) :
		for y in range(n) :
			if smell[x][y][1] != 0:
				smell[x][y][1] -= 1
			if array[x][y] != 0 :
				smell[x][y] = [array[x][y] , k]

answer = 0
while True :
	new_array = [[0] * n for _ in range(n)] # 이동 했을 때 충돌 여부를 확인해야 하므로 새로운 array
	# 상어의 위치 이동
	for x in range(n) :
		for y in range(n) :
			# 상어가 있으면 상어 이동시키기
			if array[x][y] != 0 :
				shark_move(x, y)

	# 상어 모두 이동하면, array 갱신
	array = new_array
	# 냄새 업데이트
	update_smell()
	answer += 1
	check = True
	for x in range(n) :
		for y in range(n) :
			# 상어가 1만 남아야 함
			if array[x][y] > 1 :
				check = False

	if check :
		break
	# 1000초가 지날 때까지 끝나지 않았다면
	if answer >= 1000 :
		answer = -1
		break

print(answer)


