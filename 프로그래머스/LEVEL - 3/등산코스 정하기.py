from collections import defaultdict
from heapq import heappop, heappush

# n : 노드 수
# gates : 출입구, sumits : 산봉우리

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1,3]
summits = [5]


def solution(n, paths, gates, summits):
	field = {}

	for A,B,time in paths:

		for x, y in ((A,B),(B,A)):
			try:
				field[x].append((y, time))
			except:
				field[x] =[(y, time)]

	intensity = [10000001] * (n+1)
	for gate in gates:
		intensity[gate] = 0

	check = set(summits)
	stack = gates

	while stack:
		target = set()

		while stack:
			now = stack.pop()

			for to, time in field[now]:
				max_time = max(intensity[now] , time)

				if intensity[to] > max_time:
					intensity[to] = max_time

					if to not in check :
						target.add(to)

		stack = list(target)

	return min([[summit, intensity[summit]] for summit in summits], key = lambda x: (x[1], x[0]))


print(solution(n, paths, gates, summits))

