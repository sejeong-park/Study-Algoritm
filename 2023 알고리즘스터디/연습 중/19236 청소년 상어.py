import sys
import copy

input = sys.stdin.readline

n = 4
array = [[None] * n for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
	data = list(map(int, input().split()))
	for j in range(4) :
		idx = 2*j
		# 방향 -1을 해야 값이 맞는다
		array[i][j] = [data[idx], data[idx + 1] - 1]

# 물고기 좌표를 찾는 함수
def find_fish(array, fish) :
	target_x, target_y = -1, -1
	for i in range(n) :
		for j in range(n) :
			# fish 번호 같다면, 좌표 반환
			if array[i][j][0] == fish :
				target_x, target_y = i, j
				break
	return target_x, target_y

# 모든 물고기들의 이동
def move_fish(shark_x, shark_y, array) :

	for fish in range(1, 17) :
		fish_x, fish_y = find_fish(array, fish)
		if (fish_x, fish_y) == (-1, -1) :
			continue
		fish_direct = array[fish_x][fish_y][1]

		# 반시계 방향으로 45도씩 최대 360도(1바퀴) 회전
		for _ in range(8) :
			fish_direct = (fish_direct + 1) % 8
			fish_nx = fish_x + dx[fish_direct]
			fish_ny = fish_y + dy[fish_direct]

			# 맵 내부에 위치한 경우 & 상어가 없는 경우
			if 0 <= fish_nx < n and 0 <= fish_ny < n and (shark_x, shark_y) != (fish_nx, fish_ny):
				# 해당 방향을 진행방향으로 확정
				array[fish_nx][fish_ny][1] = fish_direct
				# 물고기 간 위치 변경
				array[fish_nx][fish_ny], array[fish_x][fish_y] = array[fish_x][fish_y], array[fish_nx][fish_ny]
				break


# 상어의 이동할 수 있는 모든 좌표 (return 상어의 이동할 위치치
def shark_move(shark_x, shark_y, array) :
	shark_direct = array[shark_x][shark_y][1] 	# 상어의 진행 방향
	position = []
	# 최대 맵 크기의 -1 까지 이동 가능
	for _ in range(n-1) :
		shark_x += dx[shark_direct]
		shark_y += dy[shark_direct]
		# 진행 후 맵 내부에 위치해 있으며, 물고기가 존재하는 경우
		if 0 <= shark_x < n and 0 <= shark_y < n and array[shark_x][shark_y][0] != -1 :
			position.append((shark_x, shark_y))
	return position


# eat는 상어가 먹는 물고기
def dfs(shark_x, shark_y, eat, array) :
	global answer
	array = copy.deepcopy(array)

	eat += array[shark_x][shark_y][0]	# 해당 물고기 먹기
	array[shark_x][shark_y][0] = -1 	# 해당 물고기 잡아먹힘

	move_fish(shark_x, shark_y, array)	# 모든 물고기 이동
	position = shark_move(shark_x, shark_y, array) # 상어의 이동가능한 좌표 (물고기의 위치)

	if position :
		for shark_x, shark_y in position :
			dfs(shark_x, shark_y, eat, array)
	else :
		answer = max(answer, eat)
		return


shark_x, shark_y = 0,0
answer = 0
dfs(shark_x, shark_y, 0, array)
print(answer)