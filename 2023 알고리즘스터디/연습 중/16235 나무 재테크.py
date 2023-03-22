import sys
import copy
import time
from collections import deque


input = sys.stdin.readline

"""
양분 - 가장 처음에 모듵 칸에 5만큼 들어있다.
# m개의 나무 - 한 칸에 여러개의 나무가 심어져 있을 수도 있다.

# 나무의 성장
# 봄
나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다.
- 나무는 자신의 칸에 있는 양분만 먹을 수 있다.
- 한칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
- 만약 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.

# 여름
봄에 죽은 나무가 양분으로 변하게 된다
- 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다 (소수점 아래 버림)

# 가을 
나무의 번식
- 번식하는 나무는 나이가 5의 배수여야 한다.
- 인접한 8개의 칸에 나무가 생긴다. -> 땅을 벗어나는 칸에는 나무가 생기지 않는다.

# 겨울
땅에 양분을 추가한다.
가각 칸에 추가되는 양분은 입력으로 주어진다.
"""


n, m, k = map(int, input().split())
original_array = [list(map(int, input().split())) for _ in range(n)] # 나무의 값
array = [[5 for _ in range(n)] for _ in range(n)]
trees = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m) :
	x, y, z = map(int, input().split())
	trees[x-1][y-1].append(z)


def spring(trees) :
	fall_tree = []
	for x in range(n) :
		for y in range(n) :
			if trees[x][y] :
				trees[x][y].sort()
				tmp_tree = [] # 현재 것과 변경해줄 친구
				die = 0 # 같은 칸에 연산이 다 끝나야 한다.
				for age in trees[x][y] :
					if array[x][y] >= age :
						array[x][y] -= age
						tmp_tree.append(age+1) # 나이 한살 추가
					else:
						die += age // 2
				trees[x][y] = tmp_tree # 살아 있는 나무
				array[x][y] += die # 비료 있는 데에다가 추가해준다.

	fall(trees)

def fall(trees):
	# 나무의 번식
	for x in range(n) :
		for y in range(n) :
			if trees[x][y] :
				for age in trees[x][y] :
					if age % 5 == 0:
						for i in range(8) :
							nx = x + dx[i]
							ny = y + dy[i]
							if 0 <= nx < n and 0 <= ny < n :
								trees[nx][ny].append(1)


def winter():
	# 각 땅에 양분 추가
	for x in range(n) :
		for y in range(n) :
			array[x][y] += original_array[x][y]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


# k 년 후
for year in range(k):
	spring(trees) # tree 갱신
	winter()

result = 0
for x in range(n) :
	for y in range(n) :
		if trees[x][y] :
			result += len(trees[x][y])

print(result)



