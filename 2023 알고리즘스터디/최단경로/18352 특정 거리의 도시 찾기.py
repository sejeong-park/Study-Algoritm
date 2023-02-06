# 18352 - 특정 거리의 도시 찾기
import heapq
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
INF = int(1e9)
distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append((b, 1))

def dijkstra(start):
	queue = []
	heapq.heappush(queue, (0, start))
	distance[start] = 0 # 시작 거리 초기화

	while queue:
		dist, now = heapq.heappop(queue)
		if distance[now] < dist:
			continue

		for node in graph[now]:
			cost = dist + node[1]
			if cost < distance[node[0]]:
				distance[node[0]] = cost
				heapq.heappush(queue, (cost, node[0]))

dijkstra(x)

flag = 0
# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
	# 도달할 수 없는 경우, 무한 (INFINITY)이라고 출력
	if distance[i] == k:
		print(i)
		flag = 1

if flag == 0:
	print(-1)
