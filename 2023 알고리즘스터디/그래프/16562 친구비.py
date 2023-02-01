# 16562 친구비
# union-find
from copy import deepcopy

# 노드 n / 간선 m
n, m, k = map(int, input().split())
friends_cost = list(map(int, input().split())) # 친구 비 (0~4 -> index 차 존재)
parent = [i for i in range(n+1)]# 부모 번호

# 부모 찾기
def find_parent(parent, x) :
	if parent[x] != x:
		parent[x] = find_parent(parent, parent[x])
	return parent[x]

# 친구 찾기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)

	# 더 싼 가격이 루트 노드가 된다.
	if friends_cost[a-1] < friends_cost[b-1] :
		parent[b] = a
	else:
		parent[a] = b

for _ in range(m) :
	a, b = map(int, input().split())
	union_parent(parent, a, b)

total = 0
for index, node in enumerate(parent) :
	if index == node and index != 0:	# index 0 생략
		total += friends_cost[index-1]

# total = sum([friends_cost[index-1] for index in set(parent) if index-1 >= 0 ])

# 친구비가, 준석이가 가진 돈보다 작으면 Oh no
if total > k:
	print("Oh no")
else:
	print(total)

