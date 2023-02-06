# 플로이드 워셜 알고리즘
# 모든 정점에서 모든 정점으로 최단 거리
# 거쳐가는 정점을 기준으로 한다.

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1,n+1):
	for j in range(1, n+1) :
		if i == j:
			graph[i][j] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m) :
	a,b,c = map(int, input().split())
	graph[a][b] = c
print(graph)
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1) :
	for a in range(1, n+1) :
		for b in range(1, n+1) :
			# 간선 구하기
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n+1) :
	for b in range(1, n+1) :
		# 도달할 수 없는 경우, 무한(INF) 라고 출력
		if graph[a][b] == INF:
			print("INF", end = " ")
		else:
			print(graph[a][b], end = " ")
	print()

"""
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""
