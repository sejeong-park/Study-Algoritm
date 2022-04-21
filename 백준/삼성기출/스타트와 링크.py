from itertools import permutations

n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
def dfs(idx, cnt):
    global answer
    if cnt == n//2:
        start, link = 0,0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += array[i][j]
                elif not select[i] and not select[j]:
                    link += array[i][j]

        answer = min(answer, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt+1)
        select[i] = 0

select = [0 for _ in range(n)]
answer = 1e9
dfs(0,0)
print(answer)
