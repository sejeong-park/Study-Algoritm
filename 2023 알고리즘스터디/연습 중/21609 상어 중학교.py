# 21609 - 상어 중학교
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 블록 그룹 찾기
def bfs(x, y, color) :

	queue = deque([(x, y)])
	block_group, rainbow = [(x, y)], []
	visited[x][y] = 1

	while queue:
		x, y = queue.popleft()

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] :
				if array[nx][ny] == color :
					queue.append((nx, ny))
					visited[nx][ny] = 1
					block_group.append((nx, ny))
				if array[nx][ny] == 0 :
					queue.append((nx, ny))
					visited[nx][ny] = 1
					rainbow.append((nx, ny))


	# 무지개는 방문 해제
	for x, y in rainbow :
		visited[x][y] = 0

	return block_group, rainbow


def remove(target) :
	point = 0
	for x, y, in target :
		array[x][y] = -2 	# 없어졌다는 것을 구분하기
		point += 1

	return point

def gravity(array) :
	#
	for y in range(n) :
		empty = 0
		# 역순으로 탐색
		for index in range(n-1, -1, -1) :
			if array[index][y] == -2 :
				empty += 1
			elif array[index][y] == -1 :
				empty = 0 		# 벽임을 명시
			else :
				# 무지개 색과 일반색만 이동
				if index + empty != index:
					array[index + empty][y] = array[index][y]
					array[index][y] = -2


def rotate_90(array) :
	# 반시계 방향으로 90도 회전
	new_array = [[0] * n for _ in range(n)]

	for x in range(n):
		for y in range(n) :
			new_array[n-1-y][x] = array[x][y]

	return new_array


while True :
	# 블록 그룹 찾기
	visited = [[0] * n for _ in range(n)]
	# 크기가 가장 큰 블록을 찾을
	total_block_group = []
	for i in range(n) :
		for j in range(n) :
			if array[i][j] > 0 and visited[i][j] == 0:
				block_group, rainbow = bfs(i, j, array[i][j])
				if len(block_group + rainbow) >= 2:
					total_list = block_group + rainbow
					total_list.sort()
					total_block_group.append([len(block_group) + len(rainbow) ,len(rainbow), block_group,total_list])

	# 만약 최대 리스트를 만들 것이 없다면 반복 종료
	if not total_block_group :
		break

	# 블록의 크기, rainbow, 행, 열 순서대로 비교
	total_block_group.sort(reverse = True)
	# print(total_block_group)
	target = total_block_group[0][3]  # 전체 그룹에서 제일 첫번째

	result += remove(target) ** 2

	gravity(array)
	array = rotate_90(array)
	gravity(array)

print(result)