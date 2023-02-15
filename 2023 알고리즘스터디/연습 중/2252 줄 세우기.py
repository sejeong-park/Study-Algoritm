# 2252 줄세우기

from collections import deque


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]

for _ in range(m) :
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1


def topology_sort():
	result = []
	queue = deque()

	for i in range(1, n+1):
		if indegree[i] == 0:
			queue.append(i)

	while queue:

		now = queue.popleft()
		result.append(now)
		for i in graph[now]:
			indegree[i] -= 1
			if indegree[i] == 0:
				queue.append(i)

	print(*result)

topology_sort()
