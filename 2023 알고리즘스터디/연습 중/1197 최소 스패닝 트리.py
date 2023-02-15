# 1197 최소 스패닝 트리
# 크루스칼 알고리즘 - 핵심은 간선의 길이를 기준으로 정렬해야한다는 점
# parent는 자기 자신 노드로 초기화 하고 시작한다는 점!

v, e = map(int, input().split())
parent = [i for i in range(v+1)]	# 부모노드를 자기 자신으로 초기화해준다.
edges = []

for _ in range(e):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()	# 간선 기준으로 정렬하기

def find_parent(parent, x) :
	# 부모노드와 현재 노드가 같지 않다면, 부모노드 재귀적으로 탐색
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])

	return parent[x]

def union_parent(parent, a, b):
	# 최종적인 부모 노드로 비교
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	# 더 작은 값이 부모노드
	if a < b:
		parent[b] = a
	else:
		parent[a] = b


result = 0
for edge in edges:
	cost, a, b = edge
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost
print(result)


