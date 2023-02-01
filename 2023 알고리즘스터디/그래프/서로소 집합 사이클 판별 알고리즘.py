# 서로소 집합 사이클 판별 알고리즘

# 특정한 원소가 속한 집합 찾기
def find_parent(parent, x) :
	# 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
	if parent[x] != x:
		find_parent(parent, parent[x])
	return parent[x]

# union 두 집합 합치기
def union_parent(parent, a, b):
	a = find_parent(parent, a)
	b = find_parent(parent, b)
	if a < b:
		parent[b] = a
	else:
		parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
	parent[i] = i

cycle = False 	# 사이클 발생 여부

for i in range(e) :
	a, b = map(int, input().split())
	# 사이클이 발생한 경우 종료 -> 경로 압축 기법을 활용하여, 루트 노드까지 탐색하기 때문에 사이클 판별이 가능
	if find_parent(parent, a) == find_parent(parent, b) :
		cycle = True
		break
	# 사이클이 발생하지 않았다면, 합집합(union) 수행
	else:
		union_parent(parent, a, b)

if cycle :
	print("사이클이 발생했습니다.")
else:
	print("사이클이 발생하지 않았습니다.")