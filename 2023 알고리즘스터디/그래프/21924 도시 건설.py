# 21924 - 도시 건설
n, m = map(int, input().split())
# 간선의 개수
edges = []
for _ in range(m):
	a, b, cost = map(int, input().split())
	edges.append((cost, a, b))

edges.sort()
result = 0
parent = [0] * (m+1)	# 간선 table

for i in range(1, m+1) :
	parent[i] = i

def find_parent(parent, x) :
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

def union_parent(parent, a, b) :
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	#
	if a < b :
		parent[b] = a
	else:
		parent[a] = b


for cost, a, b in edges:
	if find_parent(parent, a) != find_parent(parent, b) :
		union_parent(parent, a, b)
		result += cost

print(result)




