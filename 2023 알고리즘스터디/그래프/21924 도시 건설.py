# 21924 도시 건설
# 크루스칼 알고리즘
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
edges = []	# 간선 집합

total, result = 0,0
for _ in range(m):
	a, b, cost = map(int, input().split())
	total += cost
	edges.append((cost, a, b))

edges.sort()

def find_parent(parent, x):
	# 더 탐색할 부모 노드가 없을 경우
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	if a < b:
		parent[b] = a
	else:
		parent[a] = b

for cost, a, b in edges:
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost

cnt = 0
for i in range(1, n+1):
	if i == parent[i]:
		cnt+=1

if cnt >= 2:
	print(-1)
else:
	print(total - result)
