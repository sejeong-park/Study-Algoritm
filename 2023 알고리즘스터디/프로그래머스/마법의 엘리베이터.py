# 프로그래머스 - 마법의 엘리베이터
storey = 2554

answer = 0
while storey :
	remainder = storey % 10
	# 6 ~ 9
	if remainder > 5:
		answer += (10 - remainder)
		storey += 10
	# 0 ~ 4
	elif remainder < 5:
		answer += remainder
	# 5
	else:
		if (storey // 10) % 10 > 4:
			storey += 10
		answer += remainder

	storey //= 10

print(answer)