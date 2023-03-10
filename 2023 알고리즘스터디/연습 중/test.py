size_info = [90,95,80,85,100,110]
shirts_info = [[90,5000], [100,4000],[110,6000]]


def solution(size_info, shirts_info) :
	answer = 0

	for size in size_info :
		min_money, check = int(1e9), int(1e9)
		for target_size, money in shirts_info :
			if size - 5 <= target_size <= size + 5:
				min_money = min(min_money, money)
			if size <= target_size :
				check = min(check, money)
		if min_money == int(1e9):
			min_money = check
		answer += min_money
	return answer
print(solution(size_info, shirts_info))
