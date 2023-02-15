# 15486 퇴사 2
n = int(input())
t = [0] * (n+2)
p = [0] * (n+2)
dp = [0] * (n+2)

for i in range(1, n+1):
	t[i], p[i] = map(int, input().split())

for i in range(1, n+1):
	end_date = i + t[i]
	if end_date <= n+1 :
		dp[end_date] = max(dp[end_date], dp[i] + p[i]) # 그냥 그대로
	dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))