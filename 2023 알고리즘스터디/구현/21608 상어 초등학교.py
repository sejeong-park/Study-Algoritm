# 21608 - 상어 초등학교

n = int(input())
# 가장좋아하는 학생 4명 조사
student = dict()
for _ in range(n*n):
	array = list(map(int, input().split()))
	student[array[0]] = array[1:]
seat = [[0]* n for _ in range(n)]	# n * n의 좌석 배치

# 자리 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 , 1]

# 조건 1 : 비어있는 칸 중 좋아하는 학생이 인접한 칸에 가장 많은 가?
def lover_check(x, y, key) :
	lover_cnt = 0 # 좋아하는학생
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n:
			if seat[nx][ny] in student[key]:
				lover_cnt += 1
	return lover_cnt

# 조건 2 : 조건 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다
def empty_seat(x, y):
	empty_cnt = 0
	for i in range(4):
		nx = x + dx[i]
		ny = y + dy[i]
		if 0<=nx<n and 0<=ny<n and seat[nx][ny] == 0:
			empty_cnt += 1
	return empty_cnt

# key 는 학생의 번호
# value는 좋아하는 학생의 번호
for key, value in student.items():
	lover_cnt_list = dict()	# 좋아하는 학생이 주변에 가장 많은 (x,y)를 담을 리스트

	for i in range(n):
		for j in range(n):
			if seat[i][j] == 0:	# 좌석이 빈자리라면
				# 첫번째 조건 탐색
				lover_cnt = lover_check(i, j, key)
				if lover_cnt not in lover_cnt_list :
					lover_cnt_list[lover_cnt] = [] 	# 여러 좌표일 수 있으므로 리스트 형태로 저장
				lover_cnt_list[lover_cnt].append((i,j))

	max_lover_cnt = max(lover_cnt_list.keys())	# 주변에 좋아하는 학생이 가장 큰 좌표에 key(학생 자리 지정)

	# 만약 좋아하는 학생이 가장 큰 게 좌표 1개 뿐이라면
	if len(lover_cnt_list[max_lover_cnt]) == 1:
		final_x, final_y = lover_cnt_list[max_lover_cnt][0]	# 첫번째 튜플
		seat[final_x][final_y] = key 	# 좌석 배치 완료

	# 만약 좋아하는 학생이 가장 많은 좌석이 여러개 이면, 주변에 빈 좌석 수가 우선순위가 되어 지정
	else:
		empty_cnt_list = dict()

		for i, j in lover_cnt_list[max_lover_cnt]:
			empty_cnt = empty_seat(i,j)
			if empty_cnt not in empty_cnt_list:
				empty_cnt_list[empty_cnt] = []	# 동일한 결과 좌표값이 여러개일수 있음
			empty_cnt_list[empty_cnt].append((i, j))

		max_empty_cnt = max(empty_cnt_list.keys())

		# 만약 주변 빈좌석 수도 겹치면
		if len(empty_cnt_list[max_empty_cnt]) != 1:
			# 조건 3: 2를 만족하는 칸도 여러 개인 경우에 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면, 열의 번호가 가장 작은 칸으로 자리를 정한다
			empty_cnt_list[max_empty_cnt].sort(key = lambda x : (x[0], x[1]))

		final_x, final_y = empty_cnt_list[max_empty_cnt][0]	# 첫번째 튜플
		seat[final_x][final_y] = key		# 	좌석 배치 완료

# print(seat)

# 학생 만족도 총 합
result = 0

for i in range(n):
	for j in range(n):
		cnt = lover_check(i, j, seat[i][j])
		if cnt == 1:
			result += 1
		elif cnt == 2:
			result += 10
		elif cnt == 3:
			result += 100
		elif cnt == 4:
			result += 1000

print(result)

