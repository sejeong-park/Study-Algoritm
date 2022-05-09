# 투포인터, 이진탐색으로 풀기 가능
#
# n, m = map(int, input().split())
# a = [int(input()) for _ in range(n)]
#
# start, end = 0,0
# min_value = 1e9
# a.sort()
# # 인덱스로 찾기 때문 (0~n-1)
# while end < n and start < n:
#     # 차가 m 미만이면, end를 계속 증가
#     if a[end] - a[start] < m:
#         end +=1
#     # 차가 m 이상을 갱신하면 start값 증가
#     else:
#         min_value = min(min_value, a[end]-a[start])
#         start += 1
#
# print(min_value)


n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
start, end = 0, 0
min_value = int(2e9)
while start < n and end < n:
    if a[end] - a[start] < m:
        end += 1
    else:
        min_value = min(min_value, a[end] - a[start])
        start += 1
print(min_value)

