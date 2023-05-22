def change_binary(n):
	tmp = []
	# 2진법 -> n/2 = 3 -- 0 3/2 -- 1 1 -> 110 (2를 계속 나눠준다음 reverse)
	while True:
		re = n % 2
		n = n // 2
		tmp.append(re)
		if n < 2:
			if n != 0 : tmp.append(n)
			break
	tmp.sort(reverse=True)
	return ''.join(list(map(str, tmp)))

def solution(s):
	answer = [0, 0]

	turn_cnt = 0
	zero_cnt = 0
	while True:
		if s == "1":
			# 이진 변환 이전 값이 10
			break
		turn_cnt += 1
		a = len(s.replace('0', ''))  # a 0 제거하여 변환한 수
		print("a ", a)
		zero_cnt += len(s) - a
		s = change_binary(a)

	return [turn_cnt, zero_cnt]

print(solution("110010101001"))