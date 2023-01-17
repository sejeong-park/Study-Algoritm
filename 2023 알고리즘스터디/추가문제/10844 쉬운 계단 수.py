# 10844 - 쉬운 계단 수

n = int(input())

dp = [[0] * 10 for _ in range(n+1)]

# 1의 자리 수는 0을 제외하고 (0은 올 수 없음) -> 1로 초기화
for i in range(1, 10):
	dp[1][i] = 1
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.
mod = 1000000000
# 2의 자리수부터 카운팅 시작
# dp[N 자리수][]
for i in range(2, n+1) :
	# 숫자를 의미하는거
	for j in range(10) :
		# 뒷자리가 0 일 때는 앞에 1밖에 오지 못함
		if j == 0:
			dp[i][j] = dp[i-1][1]
		# 뒷자리가 9 일 때는 앞에 8밖에 오지 못함
		elif j == 9 :
			dp[i][j] = dp[i-1][8]
		# 뒷자리가 2~8일때는 앞에 숫자가 2개씩 올 수 있음
		else:
			dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % mod)