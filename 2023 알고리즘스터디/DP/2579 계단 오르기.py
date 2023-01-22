# 2579 - 계단 오르기

n = int(input())
stairs = [0] * 301	# 계단 300개라는 조건 ([0] * n할 때는 IndexError가 나왔음)
for i in range(n):
	stairs[i] = int(input())

d = [0] * 301

d[0] = stairs[0]
d[1] = stairs[0] + stairs[1]	# 한 계단 오른 경우
d[2] = max(stairs[2] + stairs[1] , stairs[2] + stairs[0])	# 두 계단 오른 경우

for i in range(3, n):
	# i가 밟을 계단
	d[i] = max(stairs[i] + stairs[i-1] + d[i-3], stairs[i] + d[i-2])


print(d[n-1])