
# 14888 연산자 끼워넣기
from collections import deque

n = int(input())
array = list(map(int, input().split()))
add, minus, multi, div = map(int, input().split())


max_value = -int(1e9)
min_value = int(1e9)

def dfs(index , now, add, minus, multi, div):
	global max_value, min_value
	if index == n:
		max_value = max(max_value, now)
		min_value = min(min_value, now)
		return

	if add > 0 :
		dfs(index + 1, now + array[index], add-1, minus, multi, div)
	if minus > 0:
		dfs(index + 1, now - array[index] , add, minus - 1, multi, div)
	if multi > 0:
		dfs(index + 1, now * array[index], add, minus, multi-1, div)
	if div > 0 :
		dfs(index + 1, int(now / array[index]), add, minus, multi, div - 1)

dfs(1, array[0], add, minus, multi, div)
print(max_value)
print(min_value)