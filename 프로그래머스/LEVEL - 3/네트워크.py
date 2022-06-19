# 프로그래머스 고득점 키트 - 네트워크

n = 3
computers = [[1,1,0], [1,1,0], [0,0,1]]

def DFS(n, computers, start, visited):
    visited[start] = True

    for i in range(n):
        if visited[i] == False and computers[start][i] == 1:
            visited = DFS(n, computers, i, visited)
    return visited


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for start in range(0,n):
        if (visited[start] == False):
            DFS(n, computers, start, visited)
            answer += 1

    return answer

print(solution(n, computers))