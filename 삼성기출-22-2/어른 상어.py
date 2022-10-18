# 19347 - 어른 상어
from collections import deque


def smell_list():
	smell = [[[0,0]] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			# 냄새가 존재하는 경우, 시간을 1만큼 감소 시키기
			if smell[i][j][1] > 0:
				smell[i][j][1] -= 1
			# 상어가 존재하는 해당 위치의 냄새를 k로 설정
			if array[i][j] != 0:
				smell[i][j][1] = [array[i][j], k]
	return smell

def partition_list(target_list, n):
	return [target_list[i:i+n] for i in range(0, len(target_list),n)]

n, m, k = map(int, input().split())
# 상어의 자연수 번호
array = [list(map(int, input().split())) for _ in range(n)]
now_direction_list = map(int, input().split())
total_direction_list = [list(map(int, input().split())) for _ in range(m*4)]

# 상, 하, 좌, 우
# 1, 2, 3, 4
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# index 는 상, 하, 좌, 우

def make_direction():
	shark_direction_list = dict()
	for shark_num, shark_direct in enumerate(partition_list(total_direction_list, 4)):
		shark_direction_list[shark_num+1] = dict()
		for i in range(4):
			shark_direction_list[shark_num+1][i+1] = shark_direct[i]
	return shark_direction_list

def move_shark():
	new_array = [[0]*n for _ in range(n)]	# 임시 결과 테이블 초기화
	for x in range(n):
		for y in range(n):
			if array[x][y] > 0:
				shark_num = array[x][y]  # shark_num
				found = False
				now_direction = now_direction_list[shark_num - 1]
				# 상어의 방향 > 현재의 방향 -> 방향 우선순위
				direction_list = total_direction_list[shark_num][now_direction]

				for i in range(4):
					key = direction_list[i]
					nx = x + dx[key]
					ny = y + dy[key]

					if 0 <= nx < n and 0<= ny < n:
						# 냄새가 아무것도 없다면
						if smell[nx][ny] == 0 :
							smell[nx][ny] += 1
							# 방향 리스트에 순서 저장
							now_direction_list[shark_num-1] = key
							# 상어 다음 위치를 이동시키기
							if new_array[nx][ny] == 0:
								new_array[nx][ny] = array[x][y]
							# 만약 이미 다른 상어번호가 있다면
							else:
								# 상어가 더 작은거가 대체됌
								new_array[nx][ny] = min(new_array[nx][ny], array[x][y])

							# 상어의 이동을 찾았을 경우
							found = True
							break

				if found:
					continue
				# 주변에 냄새가 남아 있다면 자신의 냄새가 있는 곳으로 이동
				for i in range(4):
					key = direction_list[i]
					nx = x + dx[key]
					ny = y + dy[key]
					if 0<= nx < n and 0<= ny < n:
						# smell에는 [shark_num, k]
						# 자신의 냄새가 있는 곳이라면
						if smell[nx][ny][0] == array[x][y]:
							now_direction_list[shark_num-1] = key
							new_array[nx][ny] = array[x][y]
							break

	return new_array



shark_direction_list = make_direction()
smell = smell_list()
# 무한 반복
# while True:



