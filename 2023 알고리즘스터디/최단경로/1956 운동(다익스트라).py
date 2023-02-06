# 1956 다익스트라

import heapq
import sys
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (n+1) for _ in range(n+1)]
queue = []

def dijkstra():
	while queue:
		dist, start, end = heapq.heappop(queue)

		# 출발점과 도착점이 같다면, 사이클 !
		# 힙에서 뽑은 경로이기 때문에 해당 값이 최소 경로가 된다.
		if start == end:
			print(dist)
			break

		if distance[start][end] < dist : continue

		for node in graph[end] :
			cost = dist + node[0]
			if cost < distance[start][node[1]]:
				distance[start][node[1]] = cost
				heapq.heappush(queue, [cost, start, node[1]])
	else:
		print(-1)

for _ in range(m):
	a, b, cost = map(int, input().split())
	graph[a].append([cost, b])
	distance[a][b] = cost
	heapq.heappush(queue, [cost, a, b])

dijkstra()