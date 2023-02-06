# 1956 운동

n, m = map(int, input().split())
INF = int(1e9)
array = [[INF] * (n+1) for _ in range(n+1)]

# for a in range(1, n+1):
# 	for b in range(1, n+1):
# 		if a == b:
# 			array[a][b] = 0

# 각 간선 정보 입력
for _ in range(m) :
	a, b, c = map(int, input().split())
	array[a][b] = c

for k in range(1, n+1):
	for a in range(1, n+1):
		for b in range(1, n+1):
			array[a][b] = min(array[a][k] + array[k][b], array[a][b])


result = INF
for a in range(1, n+1):
	for b in range(1, n+1):
		if a != b:
			result = min(result, array[a][b] + array[b][a])

if result == INF:
	print(-1)
else:
	print(result)

result = INF
for i in range(1, n+1) :
	result = min(result, array[i][i])

print(result)