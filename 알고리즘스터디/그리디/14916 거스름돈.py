
n = int(input())
result = 0
while True:
	if n % 5 == 0:	# 만약 5원이면,
		result += n // 5 # 몫 result
		break
	else:	# 5로 나누어 떨어지지 않는 다면,
		n -= 2	# 2적용
		result += 1

	if n < 0 :
		break

if n<0:
	print(-1)

else:
	print(result)

