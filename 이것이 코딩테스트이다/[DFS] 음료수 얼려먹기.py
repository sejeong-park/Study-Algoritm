n,m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    # 1이 아니라면 -> 깊이 탐색 해야 함
    if graph[x][y]==0:
        graph[x][y]=1 # 해당 노드 방문 처리
        # 상하 좌우 모두 재귀적 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    # 더 들어갈 것이 없으면 False로 반환
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)
