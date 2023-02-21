# 1890 점프
# DFS와 DP
# n = int(input())
# array = [list(map(int, input().split())) for _ in range(n)]
#
#
# dp = [[-1]*n for _ in range(n)]
#
# cases = [(0,1) , (1, 0)]
#
# def dfs(x, y):
# 	if x == n-1 and y == n-1:
# 		return 1
#
# 	if dp[x][y] != -1:
# 		return dp[x][y]
# 	else:
# 		dp[x][y] = 0
# 		for case in cases:
# 			dx = x + case[0] * array[x][y]
# 			dy = y + case[1] * array[x][y]
# 			if 0<=dx<n and 0<=dy<n:
# 				dp[x][y] += dfs(dx,dy)
# 	return dp[x][y]
#
# print(dfs(0,0))


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
cases = [(0,1), (1,0)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
	for y in range(n):
		if x == n-1 and y == n-1:
			print(dp[x][y])
			exit(0)

		dist = array[x][y]
		if x + dist < n:
			dp[x + dist][y] += dp[x][y]
		if y + dist < n:
			dp[x][y + dist] += dp[x][y]