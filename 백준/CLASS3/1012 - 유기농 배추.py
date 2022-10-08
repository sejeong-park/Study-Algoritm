# 유기농 배추
# DFS 문제 !
import sys
sys.setrecursionlimit(10000)
t = int(input())
answer_list = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(x,y):
    graph[x][y] = -1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if graph[nx][ny] == 1:
                dfs(nx,ny)

    return


# 테스트 케이스
for _ in range(t):
    # 가로길이, 세로 길이, 배추가 심어져 있는 위치의 개수
    m, n, k = map(int, input().split())
    # 지도 그리기
    graph = [[0]*m for _ in range(n)]

    # 배추 심어진 위치 올리기
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1

    answer = 0

    # 현재 위치에서 배추지렁이 세기
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i,j)
                answer += 1

    print(answer)

# for idx in answer_list:
#     print(idx)


