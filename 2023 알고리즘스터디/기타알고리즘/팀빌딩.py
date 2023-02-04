# 22945 팀빌딩

n = int(input())
array = list(map(int, input().split()))

total, start, end = 0, 0, n-1

while start < end:
	# 다른 개발자 수 * min(A개발자 능력치, B개발자 능력치)
	target = (end- start - 1)* min(array[start], array[end])
	total = max(target, total)

	if array[start] < array[end]:
		start += 1
	else:
		end -= 1

print(total)


