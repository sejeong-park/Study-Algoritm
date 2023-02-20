# 1890 점프

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


dp = [[-1]*n for _ in range(n)]

cases = [(0,1) , (1, 0)]

def dfs(x, y):
	if x == n-1 and y == n-1:
		return 1

	if dp[x][y] != -1:
		return dp[x][y]
	else:
		dp[x][y] = 0
		for case in cases:
			dx = x + case[0] * array[x][y]
			dy = y + case[1] * array[x][y]
			if 0<=dx<n and 0<=dy<n:
				dp[x][y] += dfs(dx,dy)
	return dp[x][y]

print(dfs(0,0))