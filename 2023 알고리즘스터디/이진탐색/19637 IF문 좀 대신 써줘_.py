# 19637 IF문 좀 대신 써줘

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = []
for _ in range(n):
	name, power = input().split()
	array.append((name, int(power)))

def binary_search(array , target):
	start, end = 0, len(array)-1

	while start <= end :
		mid = (start + end) // 2

		if array[mid][1] < target :
			start = mid + 1
		else:
			end = mid - 1
	return array[end+1][0]

for _ in range(m):
	target = int(input())
	print(binary_search(array, target))