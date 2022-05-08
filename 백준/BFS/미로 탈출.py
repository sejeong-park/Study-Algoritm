from collections import deque

n, m = map(int, input().split())
array = [list(map(int, input())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
x,y = 0,0
def bfs(x,y):
    queue = deque([(x,y)])

    while queue:
        print(array)
        x, y = queue.popleft()  # 큐의 첫번째를 뽑아 x,y

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]  # 예상 범위로 step

            if 0<=nx and nx<n and 0<=ny and ny<m:
                # 만약 입력받았던 그래프가 1이면 (지나갈 수 있다면?)
                if array[nx][ny] == 1:
                    array[nx][ny] = array[x][y]+1
                    # 큐에 nx, ny 추가
                    queue.append((nx,ny))
                # 벽인 경우는 무시!!!
                else:
                    continue

    return array[n-1][m-1]  # 마지막 미로 탈출점 (0부터 시작이므로 -1)

print("결과:", bfs(x,y))

"""
5 6
101010
111111
000001
111111
111111
"""