import heapq


def dijkstra(graph, start):
	distances = {node: float('inf') for node in graph}
	distances[start] = 0
	queue = []
	heapq.heappush(queue, [distances[start], start])

	while queue:
		current_distance, current_destination = heapq.heappop(queue)
		# 기존에 있는 거리보다 길다면 볼 필요도 없음
		if distances[current_destination] < current_distance :
			continue

		for new_destination, new_distance 