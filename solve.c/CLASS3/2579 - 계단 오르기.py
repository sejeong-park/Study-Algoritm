n = int(input())
score = [0]*301
dp = [0]*301
for i in range(n):
    score[i] = int(input())

dp[0] = score[0]
dp[1] = score[0] + score[1]
# 첫번째 계단을 밟고 두 계단을 올랐을 때 합과 두번째계단을 밟고 한 계단을 올랐을 때 합 중 큰 값
dp[2] = max(score[1]+score[2], score[0]+score[2])

# 1. 마지막 계단의 전 계단을 밟은 경우
# 2. 마지막 계단의 전 계단을 밟지 않은 경우
for idx in range(3, n):
    # 3칸 밑까지 올라오는 최대 점수 + 1칸 밑의 점수 +자신의 위치 점수, 2칸 밑의 점수 + 자신의 위치 점수
    # 마지막 계단의 전계단과 전전단계까지 계단을 밟은 경우  /     마지막 계단의 전전 계단을 밟은 경우
    dp[idx] = max(dp[idx - 3] + score[idx - 1] + score[idx], dp[idx - 2] + score[idx])


print(dp[n-1])
