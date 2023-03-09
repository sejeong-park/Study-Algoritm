# 20056 마법사 상어와 파이어볼
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
array = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def move() :
	global array
	new_array = [[[] for _ in range(n)] for _ in range(n)]
	for x in range(n) :
		for y in range(n) :
			# 원소가 있다면, 이동
			if len(array[x][y]) > 0 :
				for m, s, d in array[x][y] :
					nx = (x + dx[d] * s) % n
					ny = (y + dy[d] * s) % n
					new_array[nx][ny].append((m, s, d))

	array = new_array
	# print(array)

def fireball(x, y) :
	total_m, total_s, case_1, case_2 = 0,0,0,0
	for m, s, d in array[x][y] :
		total_m += m
		total_s += s
		if d % 2 == 0:
			case_1 += 1
		else:
			case_2 += 1

	# 4개의 파이어볼로 나누기
	direction = [0,2,4,6] if case_1 == (case_1 + case_2) or case_2 == (case_1 + case_2) else [1,3,5,7]
	array[x][y] = []
	for i in range(4) :
		if total_m // 5 > 0:
			array[x][y].append((total_m // 5, total_s // (case_1 + case_2), direction[i]))

for _ in range(m) :
	x, y, m, s, d = map(int, input().split())
	array[x-1][y-1].append((m, s, d))

# print("origin" , array)

for _ in range(k) :
	# 1번 명령 후의 과정
	move()

	for x in range(n) :
		for y in range(n) :
			if len(array[x][y]) >= 2 :
				fireball(x, y)

result = 0
# 전체 돌았으니 질량 합 구하기
for x in range(n) :
	for y in range(n) :
		for m, s, d in array[x][y] :
			result+=m

print(result)