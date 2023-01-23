# 2293 - 동전 1

n, k = map(int, input().split())
coins = list(int(input()) for _ in range(n))

d = [0] * 10001 # dp 테이블은 k를 기준
d[0] = 1
for coin in coins:
	for i in range(coin, k+1) :
		d[i] += d[i-coin]
print(d[k])
