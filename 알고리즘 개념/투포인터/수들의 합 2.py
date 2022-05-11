# 2003 - 수들의 합 2

n, m = map(int, input().split())
array = list(map(int, input().split()))

start, end = 0, 0
total, cnt = 0,0

for start in range(n):
    while end < n and total <m:
        total += array[end]
        end += 1

    if total == m:
        #print(start, end)
        cnt+=1

    total -= array[start]

print(cnt)


