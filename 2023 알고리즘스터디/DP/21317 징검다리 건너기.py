# 21317 징검다리 건너기
import copy
n = int(input())
d = [0] * (n+1)	# 칸을 건널때 최대 값
small, big = [], []
for _ in range(n-1) :
	a, b = map(int, input().split())
	small.append(a)
	big.append(b)

k = int(input())

d[1] = small[0]
if n == 2:
	print(d[1])
elif n == 3:
	print(min(small[0] + small[1], big[0]))
else:
	result1, result2 = 0, 0
	for i in range(2, n) :
		d[i] = min(d[i-2] + big[i-2] , d[i-1] + small[i-1])

	for j in range(n-3):
		dp = copy.deepcopy(d)
		dp[j+3] = d[j] + k
