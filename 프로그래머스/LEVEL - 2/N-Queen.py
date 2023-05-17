# N-Queen

def is_valid(k, array) :
	# 현재 놓은 퀸의 자리가 유효한지 확인
	for i in range(k) :
		if array[i] == array[k] :
			# 1. 세로 체크
			return False
		if abs(k - i) == abs(array[k] - array[i]) :
			# 2. 대각선 체크
			return False
	return True

def dfs(start, n, array) :

	if start == n :
		return 1

	cnt = 0 # 카운트

	for i in range(n) :
		if is_valid(start, array) :
			dfs(start+1, n, array)


def solution(n) :
	global answer

	array = [0] * n
	answer = dfs(0, n, array) 	# DFS
	return answer

print(solution(4))