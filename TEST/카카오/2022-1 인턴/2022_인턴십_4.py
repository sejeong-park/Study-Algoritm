# 다익스트라 알고리즘

import heapq
import sys

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1,3]
summits = [5]

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n)]
    print(graph)
    for a,b,c in paths:
        graph[a].append((b,c))
    print(graph)
    return answer
print(solution(n, paths, gates, summits))