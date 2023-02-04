# 2960 에라토스테네스의 체

n, k = map(int, input().split())

table = [True] * (n+1)
tmp = 0
for i in range(2, n+1):
	for j in range(i, n+1, i):
		if table[j] != False:
			table[j] = False
			tmp += 1
			if tmp == k:
				print(j)