# 11055 가장 큰 증가 부분 수열
# 최장 증가 부분 수열
import copy

n = int(input())
array = list(map(int, input().split()))

d = copy.deepcopy(array)

for i in range(n) :
	for j in range(i) :
		if array[i] > array[j] :
			d[i] = max(d[i], d[j] + array[i])

print(max(d))