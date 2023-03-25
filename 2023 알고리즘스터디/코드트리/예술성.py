# 코드트리 - 예술성
import sys
import copy
from itertools import combinations, permutations
from collections import deque

"""
예술 점수 = (그룹 a 칸 + 그룹 b 칸) * (그룹 a의 숫자 값 * 그룹 b의 숫자값) * (그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수)
그룹 간 조화로움의 값을 전부 더한 것 -> 초기 예술 점수
"""

"""
십자모양과 그 외
1. 십자 모양의 경우 통째로 반시계 방향으로 90도 회전
2. 그 외 -> 정사각형 -> 개별적으로 시계 방향으로 90도 회전
"""


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
group_array = [[""] * n for _ in range(n)] # 그룹 숫자 나타내는 함수
group_num = 0
group_dict = {}
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b, visited) :
	global group_num, group_dict

	queue = deque([(a, b)])
	target = array[a][b]
	count = 0
	same_group = [(a, b)]

	while queue :

		x, y = queue.popleft()
		visited[x][y] = True
		count += 1

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<n and not visited[nx][ny] :
				if array[nx][ny] == target :
					queue.append((nx, ny))
					visited[nx][ny] = True
					same_group.append((nx, ny))

	key = f"{group_num+1}_G{target}S{count}"
	for x, y in same_group :
		group_array[x][y] = key

	group_dict[key] = same_group

	return (key, target, count)


def find_group() :
	global group_num
	visited = [[False]*n for _ in range(n)]
	group_list = []
	for x in range(n) :
		for y in range(n) :
			if not visited[x][y] :
				group_list.append(bfs(x,y, visited))		# 숫자, 크기 가 들어있는 원소들을 넣는다.
				group_num += 1

	group_list = list(combinations(group_list, 2))
	return group_list

def same_line(a_key, b_key) :
	# 그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수의 개수를 구하는 함수
	count = 0
	for x, y in group_dict[a_key] :

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<n and 0<=ny<n:
				if group_array[nx][ny] == b_key :
					count += 1

	return count

def compare_list(a, b) :
	# 점수를 리턴하는 함수
	# (key, target, count)
	# 크기가 작은 것이 탐색 시작 - 시간 줄이기 위해
	min_group, max_group = 0, 0
	if a[2] <= b[2] :
		max_group, min_group = b, a
	else:
		max_group, min_group = a, b

	same_cnt = same_line(min_group[0],  max_group[0]) # 탐색을 시작하는 좌표값과, 맞닿는 변의 target 수

	# (그룹 a 칸 + 그룹 b 칸) * (그룹 a의 숫자 값 * 그룹 b의 숫자값) * (그룹 a와 그룹 b가 서로 맞닿아 있는 변의 수)
	return (a[2] + b[2]) * (a[1] * b[1]) * same_cnt

def find_get_point(group_list):
	total_count = 0
	for a, b in group_list :
		point = compare_list(a, b)
		if point > 0 :
			total_count += point
	# print(total_count)
	return total_count


def division(array) :
	new_array = [[0] * n for _ in range(n)]
	mid = n//2

	# 십자가 모양의 반 시계 방향 회전
	for i in range(n) :
		new_array[mid][i] = array[i][mid]
	for i in range(n) :
		new_array[i][mid] = array[mid][(n-1)-i]

	# mid의 양옆

	# 첫번째 사각형
	for i in range(mid) :
		for j in range(mid) :
			new_array[j][mid-i-1] = array[i][j]

	# 두번째 사각형
	for i in range(mid) :
		for j in range(mid+1, n) :
			new_array[j-mid-1][n-i-1] = array[i][j]

	# 세번째 사각형
	for i in range(mid+1, n) :
		for j in range(mid) :
			new_array[j+mid+1][n-i-1] = array[i][j]

	# 네번째 사각형
	for i in range(mid+1, n) :
		for j in range(mid+1, n) :
			new_array[j][n-i+mid] = array[i][j]


	# print(new_array)

	return new_array



def simulation(i):
	global group_dict, array, result

	group_dict = {}		# 초기화
	group_list = find_group()
	result += find_get_point(group_list)	# 초기 예술 점수 더한 값

	if i == 4:
		return result

	array = division(array)	# 새로운 회전


for i in range(4) :
	simulation(i)

print(result)


"""
5
1 2 2 3 3
2 2 2 3 3
2 2 1 3 1
2 2 1 1 1
2 2 1 1 1

"""