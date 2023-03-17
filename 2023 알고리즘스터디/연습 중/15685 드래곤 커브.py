# 15685 - 드래곤 커브
import sys
input = sys.stdin.readline
"""
초기 조건 : 시작점, 시작 방향, 세대
0 세대 드래곤 커브 : 길이가 1인 선분
# 0
1 세대 드래곤 커브 : 0 세대 드래곤 커브의 끝점을 기준으로 시계방향 90도 회전
# 0, 1
2 세대 드래곤 커브 : 1세대 드래곤 커브로 만든 방법을 이용해서
# 0, 1,| 2, 1 -> 반대로 뒤집으면 : 2, 3, 2, 1
3 세대 드래곤 커브 : 2세대 드래곤 커브로 만ㄴ든 방법을 이용해서
# 0, 1, 2, 1 (2세대)| 2, 3 (1세대 반대)|  2, 1 -> 반대로 뒤집으면 : 
4 세대 드래곤 커브 : 3세대 드래곤 커브로 만든 방법을 이용해서
# 0, 1, 2, 1, 2, 3, 2, 1 (3세대)| 2, 3, 0, 3 (2세대 반대)|  2, 3, 2, 1
# k세대 드래곤 커브는 드래곤 커브 끝점을 기준으로 90도 시계 방향 회전시킨 다음 끝점에 붙인 것
"""

array = [[0] * 101 for _ in range(101)]
n = int(input())

# 증가 방향 : 오 - 0 | 상 - 1 | 왼 - 2 | 하 - 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


for _ in range(n) :

	x, y, d, g = map(int, input().split())
	array[x][y] = 1

	move = [d] # 0 세대
	# g 세대 만큼 반복
	for _ in range(g) :
		tmp = []
		for i in range(len(move)) :
			tmp.append((move[-i-1] + 1)%4)
		move.extend(tmp)

	# 드래곤 커브에 해당하는 좌표 추가
	for i in move :
		nx = x + dx[i]
		ny = y + dy[i]
		array[nx][ny] = 1
		x, y = nx, ny

# 모든 꼭짓점이 드래곤
answer = 0
for x in range(100) :
	for y in range(100) :
		if array[x][y] and array[x+1][y] and array[x][y+1] and array[x+1][y+1] :
			answer += 1


print(answer)




# 3
# 3 3 0 1
# 4 2 1 3
# 4 2 2 1