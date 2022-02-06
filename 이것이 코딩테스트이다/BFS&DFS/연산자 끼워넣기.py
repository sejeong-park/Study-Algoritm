# 연산자 끼워넣기

# 모든 경우의 수를 계산하기 위하여(완전 탐색) DFS 혹은 BFS를 이용해 문제를 해결 가능
# 사칙 ㅇㄴ산을 중복하여 사용할 ㅅ 있기 때문에, 중복 순열을 계산해야함.

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int,input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int,input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1

        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub +=1

        if mul > 0:
            mul -= 1
            dfs(i+1, now*data[i])
            mul+=1

        if div>0:
            div -= 1
            dfs(i+1, int(now/data[i]))
            div+=1

dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
