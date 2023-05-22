

n, d = map(int, input().split())
table = [0] * (d + 1) # 0초부터 시작
# 다이너마이트
for _ in range(n) :
	point, time = map(int, input().split())
	table[point] = time
a, b = 0, d
time = 0
while True :
	# 만약 다이너마이트가 있다면
	if a == b :
		break
	if table[a] != 0:
		table[a] -= 1
	else :
		a += 1

	if table[b] != 0:
		table[b] -= 1
	else:
		b -= 1


	time += 1
	print(a, b, time)

print('---')
print(time)

