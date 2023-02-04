
n = int(input())

final = [0] * n

def map_function(map_list):
	map_list.sort(reverse = True)

	rank, tmp = 1, 0  # 등수 초기화 / tmp은 동점자 수
	target = map_list[0][0]	# 직전 사람 비교 초기화
	map_list[0].append(rank)
	for k in range(1, n):
		if target == map_list[k][0] :
			map_list[k].append(rank)
			tmp += 1 # 동점자수 세기
		else:
			rank += (tmp+1) # 동점자 수 + 등수 증가
			tmp = 0 # 동점자 수 초기화
			map_list[k].append(rank)

			target = map_list[k][0] # 비교값은 다음으로 넘어감
	map_list.sort(key = lambda x : x[1])	# 다시 index를 기준으로 sort
	return map_list

for i in range(3):
	scores = list(map(int, input().split()))
	map_list = []	# score와, index
	for i, score in enumerate(scores):
		map_list.append([score,i])
		final[i] += score
	result = map_function(map_list)
	# 출력
	for k in range(n):
		print(result[k][-1], end = ' ')
	print()

map_list = []
for i, score in enumerate(final):
	map_list.append([score, i])
result = map_function(map_list)
for k in range(n):
	print(result[k][-1], end = ' ')

#
# 3
# 40 80 70
# 50 10 20
# 100 70 30
