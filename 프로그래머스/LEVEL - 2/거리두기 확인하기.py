# 거리두기 확인하기 - 카카오 채용연계형 인턴십
from collections import deque


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
result = [1,0,1,1,1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def rule(target, case):
    visited = [[0]*5 for _ in range(5)]
    queue = deque([target])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        if visited[x][y] == 3:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny]:
                if case[nx][ny] != 'X':
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
                if case[nx][ny] == 'P':
                    return 0
    return 1

def solution(places):
    answer = []
    # 케이스 별로 분할
    compare = 0
    for case in places:
        target_p = []
        for i in range(5):
            for j in range(5):
                if case[i][j] == 'P':
                    target_p.append((i,j))
        output = 0
        if not target_p:
            output = 1
        else:
            for i,j in target_p:
                output = max(output, rule((i,j), case))


        answer.append(output)


    print(answer)
    return answer

solution(places)
