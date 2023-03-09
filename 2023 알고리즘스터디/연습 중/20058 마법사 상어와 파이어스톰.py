# 20058 마법사 상어와 파이어스톰
from collections import deque

n, q = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(2**n)]
l_list = list(map(int, input().split()))

def rotate(board, l) :
	len_array = len(board[0])
	new_array = [[0] * len_array for _ in range(len_array)] # 회전 array 저장 용도

	# rotate
	r_size = 2** l # 격자 사이즈
	for x in range(0, len_array, r_size) :
		for y in range(0, len_array, r_size) :
			# 격자 단위
			for i in range(r_size) :
				for j in range(r_size) :
					new_array[x+j][y + r_size - i - 1] = array[x + i][y + j]
	return new_array

def melting(board) :
	global array
	melting_list = [] # 녹을 얼음 좌표
	len_array = len(board[0])
	for x in range(len_array) :
		for y in range(len_array) :
			cnt = 0 # 상하 좌우 찾기
			for i in range(4) :
				nx = x + dx[i]
				ny = y + dy[i]

				if 0 <= nx < len_array and 0 <= ny < len_array :
					if array[nx][ny] > 0 :
						cnt += 1
			# 녹는 조건 -> 녹는 조건을 모르겠음
			if cnt < 3 and array[x][y] != 0:
				melting_list.append((x, y))

	for x, y in melting_list:
		array[x][y] -= 1

	return array

def check(board):
	"""
	남아있는 얼음의 합
	남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
	조건 : 얼음이 있는 칸과 인접해 있으면 두 칸을 연결되어 있다고 한다. -> 덩어리는 연결된 칸의 집합
	:param array:
	:return:
	"""
	len_array = len(board[0])
	visited = [[False] * len_array for _ in range(len_array)]
	ice_sum, max_area = 0,0

	for i in range(len_array) :
		for j in range(len_array) :

			area_cnt = 0
			if not visited[i][j] and array[i][j] != 0:
				queue = deque([(i, j)])
				visited[i][j] = True

				while queue:
					x, y = queue.popleft()
					ice_sum += array[x][y] # 얼음의 합 추가
					area_cnt += 1 # 얼음 카운트 추가

					for d in range(4) :
						nx = x + dx[d]
						ny = y + dy[d]

						if 0 <= nx < len_array and 0 <= ny < len_array :
							if array[nx][ny] != 0 and not visited[nx][ny]:
								visited[nx][ny] = True
								queue.append((nx, ny))

				max_area = max(max_area, area_cnt)

	return ice_sum, max_area

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ice_sum, max_area = 0,0
for l in l_list :
	array = rotate(array, l) #  회전하고 갱신
	array = melting(array)

ice_sum, max_area = check(array)
print(ice_sum)
print(max_area)




