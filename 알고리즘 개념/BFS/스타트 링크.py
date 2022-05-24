# 5014 - 스타트 링크
from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0] * (F+1)

def bfs(start) :
    queue = deque([start])
    while queue:
        kangho = queue.popleft()
        if kangho == G:
            return visited[kangho]
        for move in (kangho - D, kangho + U):
            if 0 < move <= F and not visited[move] and move != start :
                visited[move] = visited[kangho] + 1
                queue.append(move)
    return "use the stairs"

print(bfs(S))


