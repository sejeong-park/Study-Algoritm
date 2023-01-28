# 11265 끝나지 않은 파티

n, m = map(int, input().split())
INF = int(1e9)
array = [list(map(int, input().split())) for _ in range(n)]

for a in range(n):
	for b in range(n):
		if array[a][b] == 0:
			array[a][b] = INF
# 플로이드 워셜 - 최단 거리 구하기
for k in range(n):
	for a in range(n):
		for b in range(n):
			array[a][b] = min(array[a][b], array[a][k] + array[k][b])

for _ in range(m):
	a, b, c = map(int, input().split())
	# 시간 안에 다른 파티장에 도착할 수 있으면
	if array[a-1][b-1] <= c:
		print("Enjoy other party")
	# 다른 파티장에 도착할 수 없으면
	else:
		print("Stay here")