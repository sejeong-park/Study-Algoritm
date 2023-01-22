import sys
n = int(input())
array = list(map(int, input().split()))

start, end = 0, (n-1) * (1+abs(array[n-1] - array[0]))

while start <= end :
	mid = (start + end) // 2
	visited = [False for _ in range(n)]
	visited[0] = True
	# 왼쪽으로 가기
	for j in range(1, n):
		# 오른쪽으로 가기
		for i in range(j) :
			if visited[i] and (j-i) * ( 1+ abs((array[j] - array[i]))) <= mid :
				visited[j] = True	# 방문
				break
	if visited[n-1] :
		end = mid - 1
	else:
		start = mid + 1

	print(start)

print(start)