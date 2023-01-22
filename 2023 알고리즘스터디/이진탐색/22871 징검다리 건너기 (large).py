# 22871 - 징검다리 건너기 (large)
#
# n = int(input())
# array = list(map(int, input().split()))
# INF = 9999999
# dp = [0] + [INF] * (n-1)
# # https://kjhoon0330.tistory.com/entry/BOJ-22781-%EC%A7%95%EA%B2%80%EB%8B%A4%EB%A6%AC-%EA%B1%B4%EB%84%88%EA%B8%B0-Python
# for i in range(1, n):
# 	for j in range(0, i):
# 		power = (i-j) * (1+abs(array[i] - array[j]))
# 		max_power = max(power, dp[j])
# 		print(i, j, power, dp[j])
# 		dp[i] = min(dp[i], max_power)
# print(dp)
# # print(dp)
# print(dp[-1])
#

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in range(i+1 ,N):
        print("{}에서 {}로 이동하는 힘 = : {}".format(i+1, j+1, ((j-i)*(1+abs(A[i]-A[j])))))