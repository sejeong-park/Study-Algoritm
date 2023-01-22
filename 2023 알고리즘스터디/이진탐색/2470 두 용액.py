# 2470 두 용액
import sys
n = int(input())
array = list(map(int, input().split()))
array.sort()

start, end = 0, n-1
INF = sys.maxsize	# system이 지정할 수 있는 최댓값

target = array[start] + array[end]
x, y = 0,0
while start < end :
	tmp = array[start] + array[end]	# 합
	if abs(tmp) < INF :
		min_value = abs(tmp)
		x, y = start, end
	if tmp < 0 :
		start += 1
	elif tmp > 0 :
		end -= 1
	else:
		break


print(array[x], array[y])

