# 코드트리 나무박멸 - 삼성 SW 역량테스트 2022 상반기 오후 2번 문제
import sys
import copy

"""
성장 -> 동시에 -> 전체 나무에 대해 돌아야 한다.
"""


def growth_tree():
	"""
	조건 1.
	인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장한다.
	성장은 모든 나무에게 동시에 일어난다.
	++++ 1년이 지나면 제초제는 1 지워진다.
	"""
	new_tree = copy.deepcopy(tree)
	for x in range(n) :
		for y in range(n) :
			if tree[x][y] > 0 :
				count = 0
				for i in range(4) :
					nx = x + dx[i]
					ny = y + dy[i]
					# 격자 밖을 벗어날 경우 count X
					if not (0<=nx<n and 0<=ny<n) :
						continue
					# 인접한 나무가 있을 때, 카운트
					if tree[nx][ny] > 0 :
						count += 1
				# 4개의 칸 중 나무가 있는 칸의 수만큼 증가
				tree[x][y] += count

	# print("조건 1. ", tree)


def tree_child() :
	"""
	조건 2.
	기존에 있었던 나무들은 인접한 4개 칸 중 벽/ 다른 나무/ 제초제 모두 없는 칸에 번식한다.
	각 칸 나무 그루 수 / 총 번식이 가능한 칸의 개수 -> 나누어진 나무 그루 수 만큼 번식이 된다. (나눌 때 생기는 나머지 버린다.)
	번식 과정은 모든 나무에서 동시에 일어나게 된다.
	"""
	new_tree = copy.deepcopy(tree)

	# tree_child 까지 끝낸 나무는 -> new_tree에 저장
	for x in range(n) :
		for y in range(n) :
			if tree[x][y] > 0:

				new_tree[x][y] = tree[x][y]

				child = []
				for i in range(4) :
					nx = x + dx[i]
					ny = y + dy[i]
					if not (0<=nx<n and 0<=ny<n) :
						continue
					# 벽 / 다른 나무가 없는 칸 -> 빈칸 / 제초제가 없는 칸
					if tree[nx][ny] == 0 and danger[nx][ny] == 0 :
						child.append([nx, ny])
				# 각 탄 나무 그루수 / 총 번식이 가능한 칸의 수
				for nx, ny in child :
					new_tree[nx][ny] += tree[x][y] // len(child)
	# print("조건 2.", new_tree)
	return new_tree

def spread_danger(tree):
	global total_result
	"""
	조건 3.
	각 칸 중 제초제를 뿌렸을 때, 나무가 가장 많이 박멸되는 칸에 제초제를 뿌린다.
	- 나무가 없는 칸에 제초제를 뿌린다. -> 박멸되는 나무가 전혀 없음 -> 모든 나무가 없으면, 제초제를 뿌릴 칸도 없다.
	- 나무가 있는 칸에 제초제를 뿌린다. -> 4개의 대각선만큼 k칸 만큼 전파되게 된다.
		- 전파 도중, 벽이나, 나무가 아예 없는 칸이 있는 경우, 그 칸까지는 제초제가 뿌려지는 경우 제초제가 전파되지 않는다.
	- 제초제가 뿌려진 칸에는 C년만큼 제초제가 남아 있다가 c+1년째가 될 때, 사라지게 된다.
		- 제초가 뿌려지는 경우에는, 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지된다.
	"""

	# 대각선 대상
	sx = [-1, -1, 1, 1]
	sy = [-1, 1, -1, 1]

	# test = [[0]*n for _ in range(n)] # 제초제 양 테스트
	danger_list = [] # 제초제가 뿌려지는 리스트를 만들자. (제초제가 뿌려질 경우에.)

	for x in range(n) :
		for y in range(n) :
			if danger[x][y] > 0 :
				danger[x][y] -= 1
			if tree[x][y] > 0 :
				# 제초제를 뿌릴 수 있는 칸 수 세기
				die_tree = tree[x][y]
				for i in range(4) :
					nx, ny = x, y 		# 처음 칸으로 초기화
					for _ in range(k) :
						nx += sx[i]
						ny += sy[i]
						if not (0<=nx<n and 0<=ny<n) :
							break
						# 벽이거나, 나무가 아예 없는 경우 -> 0, -1 -> 제초제의 확산은 막는다.
						if tree[nx][ny] <= 0 :
							# 살아남은 아이일 경우
							if tree[nx][ny] != -1 :
								die_tree += tree[nx][ny]
							break
						else:
							# 살아남은 아이일 경우
							die_tree += tree[nx][ny]
				# test[x][y] = die_tree # 테스트용
				danger_list.append((x, y, die_tree))

	# 제초제 최댓값 확인하는 테스트용
	# for i in range(n) :
	# 	print(*test[i])

	# 최대값 찾았으면 할 일들
	# 제초제를 더 뿌릴 곳도 없을 수 있다. -> 실행 안하고 넘어가
	if danger_list :
		# 나무의 수가 동일하면, 행이 작은 순서대로, 행이 같은 경우, 열이 작은 칸
		danger_list.sort(key = lambda x : (-x[2], x[0], x[1]))
		target_x, target_y = danger_list[0][0] , danger_list[0][1]

		# 제초제를 뿌릴 곳을 정했다면, 뿌리기
		total_result += tree[target_x][target_y] 		# 나무 박멸
		danger[target_x][target_y] = c 					# 제초제 뿌림
		tree[target_x][target_y] = 0 					# 나무 박멸

		# 대각선 모양으로도 박멸 & 제초제 뿌려줌
		for i in range(4) :
			nx , ny = target_x, target_y
			for _ in range(k) :
				nx += sx[i]
				ny += sy[i]
				if not (0<=nx<n and 0<=ny<n) :
					break
				# 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우, 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
				if tree[nx][ny] <= 0 :
					# 여기까지는 제초제를 뿌려준다.
					danger[nx][ny] = c
					break
				# 죽을 대상인 나무들에 대해
				danger[nx][ny] = c 			# 제초제가 원래 있어도, c 로 갱신
				total_result += tree[nx][ny]
				tree[nx][ny] = 0 			# 나무 있는 칸 박멸


	# print("조건 3. ", tree)
	# print("제초제", danger)


def simulation():
	# 1년 단위 실행 동작
	growth_tree()			# 조건 1
	tree = tree_child()	 	# 조건 2
	spread_danger(tree)		# 조건 3
	return tree


n, m, k, c = map(int, input().split())
tree = [list(map(int, input().split())) for _ in range(n)]
danger = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total_result = 0
for _ in range(m) :
	tree = simulation()

print(total_result)

"""
5 2 2 1
0 0 0 0 0
0 30 23 0 0
0 0 -1 0 0
0 0 17 46 77
0 0 0 12 0
"""