# 2565 전깃줄

n = int(input())
array = list(list(map(int, input().split())) for _ in range(n))

array.sort()
d = [1] * n

for i in range(n) :
	for j in range(i):
		# end 값 비교
		if array[i][1] > array[j][1] :
			d[i] = max(d[i], d[j] + 1)

print(n - max(d))


