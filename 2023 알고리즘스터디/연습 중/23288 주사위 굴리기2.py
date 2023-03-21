# 23288 주사위 굴리기 2
import sys
import copy
from collections import deque
"""
주사위 (1,1) / 오른쪽 3 / 밑면 1 -> 처음 이동방향 동쪽
# 주사위의 이동 한번
1. 주사위가 이동 방향으로 1칸 -> 이동방향에 칸이 없다면 이동방향을 반대로 한다음 한 칸 굴러간다
2. 주사위가 도착한 칸 (x, y)에 대한 점수 획득 (B*C)
3. 주사위 밑면 A와 (x, y)가 있는 점수 B를 비교해 이동 방향을 결정
	- A > B 인 경우 이동 방향을 90도 회전 (시계 방향)
	- A < B 인 경우 이동 방향 반대로 90도 회전 (반시계 방향)
	- A = B 인 경우 이동 방향에 변화는 없다.
# 칸에 대한 점수 (2번)
- (x, y)에 있는 정수는 B
	- (x, y)에서 동서남북 방향으로 연속해서 이동할 수 있는 칸의 수 C
	- 이동 가능한 칸에는 모두 정수 B가 있어야 함
	- 점수 = B*C
"""
input = sys.stdin.readline
n, m, k = map(int, input().split()) # k는 이동하는 횟수
array = [list(map(int, input().split())) for _ in range(n)]

# 주사위 - 윗면 기준
dice = {
	"top" : 1 ,
	"bottom" : 6 ,
	"up" : 2 ,
	"down" : 5 ,
	"left" : 4 ,
	"right" : 3
}

# 방향 - 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y, d = 0, 0, 0 	# 주사위 초기 값


def move_dice(direction) :
	new_dice = copy.deepcopy(dice)
	# 동쪽으로 이동
	if direction == 0 :
		new_dice["top"], new_dice["bottom"] = dice["left"], dice["right"]
		new_dice["right"], new_dice["left"] = dice["top"] , dice["bottom"]

	# 서쪽으로 이동
	elif direction == 2 :
		new_dice["top"], new_dice["bottom"] = dice["right"], dice["left"]
		new_dice["right"], new_dice["left"] = dice["bottom"], dice["top"]

	# 남쪽으로 이동
	elif direction == 1 :
		new_dice["top"], new_dice["bottom"] = dice["up"], dice["down"]
		new_dice["up"], new_dice["down"] = dice["bottom"], dice["top"]

	# 북쪽으로 이동
	elif direction == 3 :
		new_dice["top"], new_dice["bottom"] = dice["down"], dice["up"]
		new_dice["up"], new_dice["down"] = dice["top"], dice["bottom"]

	return new_dice

# bfs를 이용해 연속한 칸 구하기
def get_point(x, y) :
	visited = [[False] * m for _ in range(n)] # BFS 탐색을 위한 visited
	target = array[x][y]

	queue = deque([(x, y)])
	count = 1
	visited[x][y] = True


	while queue :
		x, y = queue.popleft()

		for i in range(4) :
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m and not visited[nx][ny] :
				if array[nx][ny] == target:
					queue.append((nx, ny))
					count += 1
					visited[nx][ny] = True

	# 칸에 대한 점수
	return target * count

def find_direction(a, b, d) :
	# 시계방향
	if a > b :
		d = (d+1) % 4
	elif a < b :
		d = (d-1) % 4 # 반시계 방향

	return d


result = 0  # 최종 결과
for _ in range(k) :
	# 1. 주사위 한 칸 이동
	nx = x + dx[d]
	ny = y + dy[d]
	if not (0<=nx<n and 0<=ny<m) :
		d = (d+2)%4 # 반대 방향
		nx = x + dx[d]
		ny = y + dy[d]

	# 주사위의 이동 갱신
	dice = move_dice(d)
	x, y = nx, ny

	# 2. 이동한 칸 점수 획득
	result += get_point(x, y)

	# 3. 방향 갱신
	d = find_direction(dice["bottom"], array[x][y], d) # bottom과 B의 비교
	# print("new_d: ", d, dice)

print(result)