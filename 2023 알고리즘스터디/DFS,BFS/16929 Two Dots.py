# 16929 Two Dots
from collections import deque

n, m = map(int, input().split())
array = [list(map(str, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
# print(array)

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 사이클 존재 여부 카운팅
def dfs(x, y , count, depth):
	# print(count, depth)
	visited[x][y] = True
	count[x][y] = depth		# 카운트 회전에는 depth 넣어주기
	for i in range(4) :
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<m:
			# 다음 갈 블록이 0이 카운트가 0이 아닐때(시작을 이미 했을 때)
			# 순번 탐색, 다음 갈 블록의 카운트가 DEPTh-1일때
			if count[nx][ny] != 0 and count[nx][ny] != depth - 1:
				# print("count" , count)
				print('Yes')
				exit()
			# 현재 위치와 앞으로 위치의 알파뱃이 같을 때 & 신규 카운트일때
			if array[nx][ny] == array[x][y] and count[nx][ny] == 0:
				dfs(nx, ny, count, depth+1)	# 다음 DFS 깊이, count는 유지

for i in range(n):
	for j in range(m):
		# 방문을 하지 않았다면
		count = [[0]*m for _ in range(n)]
		dfs(i,j,count, 1)

print('No')

