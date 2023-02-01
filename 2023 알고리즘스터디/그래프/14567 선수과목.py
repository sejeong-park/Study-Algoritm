# 14567 선수과목
# 위상 정렬
from collections import deque
import sys

input = sys.stdin.readline

node, line = map(int, input().split())
indegree = [0] * (node+1)
graph = [[] for _ in range(node+1)] # 노드 기준
answer = [1] * (node+1)		# 선수과목 기준을 1로 초기화


for _ in range(line):
	a, b = map(int, input().split())
	graph[a].append(b)
	indegree[b] += 1	# 진입 차수 증가



def topology_sort():

	result = []
	queue = deque()
	# 노드의 indegree가 0 인 노드 찾고 queue에 넣기
	for i in range(1,node+1):
		if indegree[i] == 0:
			queue.append(i)

	# 큐 탐색 시작
	while queue:
		now = queue.popleft()
		result.append(now)	# 결과에 큐 순서 입력

		# now 에 연관된
		for i in graph[now]:
			indegree[i] -= 1
			# 진입 값이 0으로 초기화 되면
			if indegree[i] == 0:
				queue.append(i)
				answer[i] = answer[now] + 1	 # 선수과목 (DFS 원리)

	return answer

answer = topology_sort()
for i in range(1, node+1) :
	print(answer[i], end = " ")



# 6 4
# 1 2
# 1 3
# 2 5
# 4 5




