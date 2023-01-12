# 14719 빗물

h, w = map(int, input().split())
array = list(map(int, input().split()))

result = 0
for i in range(1, w - 1):	# 첫번째 블록과 마지막 블록은 물이 고일 수 없음
	left_max = max(array[:i])	# 왼쪽 벽
	right_max = max(array[i+1:])	# 오른쪽 벽

	m = min(left_max, right_max)	# 벽의 물이 차오르는데 까지 -> 물의 높이

	if m > array[i]:	# 현재 벽의 높이가 물의 높이가 작으면 -> 물이 차는 구간
		result += m - array[i]	# 물차는 구간 더해주기

print(result)
