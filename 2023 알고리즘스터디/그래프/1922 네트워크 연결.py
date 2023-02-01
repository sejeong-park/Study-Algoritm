# 1922 - 네트워크 연결

n = int(input()) # 노드의 개수
m = int(input())
parent = [index for index in range(n+1)] # 부모 테이블
lines = []

def find_parent(parent, x) :
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

for _ in range(m):
	a, b, cost = map(int, input().split())
	lines.append((cost, a, b))

lines.sort()

result = 0
for cost, a, b in lines:
	# cycle 이 없는 경우만, union 집합이 성립
	if find_parent(parent, a) != find_parent(parent, b):
		union_parent(parent, a, b)
		result += cost


print(result)

