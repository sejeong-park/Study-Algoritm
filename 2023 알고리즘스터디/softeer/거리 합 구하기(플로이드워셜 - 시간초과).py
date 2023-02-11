import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
	for j in range(1, n+1):
		if i == j:
			graph[i][j] = 0

for i in range(n-1) :
	a, b, cost = map(int, input().split())
	graph[a][b], graph[b][a] = cost, cost

for k in range(1, n+1) :
	for a in range(1, n+1) :
		for b in range(1, n+1):
			graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
	answer = sum(graph[i][1:])
	print(answer)
