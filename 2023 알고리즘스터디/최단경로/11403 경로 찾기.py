# 11403 경로 찾기

n = int(input())

INF = int(1e9)
array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
	for j in range(n):
		if array[i][j] == 0:
			array[i][j] = INF


for k in range(n) :
	for a in range(n):
		for b in range(n) :
			array[a][b] = min(array[a][b], array[a][k] + array[k][b])


for a in range(n):
	for b in range(n):
		if array[a][b] == INF:
			array[a][b] = 0
		else:
			array[a][b] = 1

		print(array[a][b], end = " ")
	print()
