
def solution(m, n, board):
	answer = 0
	# 문자열 -> 리스트
	for i in range(m):
		board[i] = list(board[i])

	# 루프 돌기
	while True:

		delete = []
		check = False  # 만약 더 없앨 블록이 없는지 확인
		# STEP 1 : 4개가 붙어있다면, 지운다.
		for i in range(m - 1):
			for j in range(n - 1):
				if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] and board[i][j] != "0":
					delete.append((i, j))  # 각 포인트를 넣는다.
					delete.append((i + 1, j))
					delete.append((i, j + 1))
					delete.append((i + 1, j + 1))
					check = True

		if check == False:
			break

		delete = set(delete)
		answer += len(delete)  # 지워질 개수

		for i, j in delete:
			board[i][j] = "0"		# 여기서 내가 "0"처리를 해준 것을 까먹어서 STEP1에서 무한 루프 돌았음 ㅎ


		# STEP 2 : 중력구현하기 -> 바닥부터 카운트 (i에서만 변함)
		for j in range(n):
			empty = 0
			for i in range(m - 1, -1, -1):
				if board[i][j] == "0":
					empty += 1
				else:
					if i + empty != i:
						board[i + empty][j] = board[i][j]  # 중력에 의해 이동
						board[i][j] = "0"  # 빈칸 채우기

		for i in range(m):
			print(*board[i])

	return answer
test1 = solution(4,5, 	["CCBDE", "AAADE", "AAABF", "CCBBF"])
test2 = solution(6,6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"])
print(test1)