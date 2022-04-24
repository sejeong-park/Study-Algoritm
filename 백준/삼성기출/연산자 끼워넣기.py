# 14888 - 연산자 끼워넣기

from collections import deque

n= int(input())
array = list(map(int, input().split()))
add, minus, multi, division = map(int, input().split())

min_value = 1e9 # 최소값
max_value = -1e9 # 최대값

###########
def dfs(idx, now):
    global add, minus, multi, division, min_value, max_value

    if idx == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add>0:
            add -= 1
            # 다음 연산 시행
            dfs(idx+1, now + array[idx])
            add +=1
        if minus>0:
            minus -= 1
            dfs(idx+1, now - array[idx])
            minus += 1
        if multi>0:
            multi -= 1
            dfs(idx+1, now * array[idx])
            multi+=1
        if division>0:
            division -=1
            dfs(idx+1, int(now/array[idx]))
            division+=1


# 처음 시작하는 dfs
dfs(1, array[0])
print(max_value)
print(min_value)

