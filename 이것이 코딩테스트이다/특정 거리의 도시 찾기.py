# 특정 거리의 도시 찾기
# BFS (너비 우선 탐색)
from collections import deque
# 도시의 개수, 도로의 개수, 거리의 정보, 출발 도시 번호
n,m,k,x = map(int,input().split())

graph = [[] for _ in range(n+1)]    # 0으로 시작 말고, 1로 시작하기 위해 n+1로 range를 지정해 줌

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b) # 특정 노드의 index에 매칭되는 b값 지정 (도로 간 연결)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1]*(n+1)
distance[x]=0 # 출발 도시까지의 거리는 0 으로 설정

# 너비 우선 탐색(BFS) 수행
queue = deque([x])
while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[now]+1
            queue.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)
