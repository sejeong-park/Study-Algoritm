# 1520 - 내리막길
from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
dp = list([-1]*m for _ in range(n))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = []
def dfs(x,y):
	if x == n-1 and y == m-1:
		return 1
	# 탐색 유무
	if dp[x][y] == -1:
		dp[x][y] = 0

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < m:
				if array[nx][ny] < array[x][y]:
					dp[x][y] += dfs(nx, ny)
	return dp[x][y]
print(dfs(0,0))