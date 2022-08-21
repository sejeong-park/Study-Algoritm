

skills = [1,1,4,2,1,1]
team = [2,1,5]
k = 4
def solution(skills, team, k):
	answer = 0
	maximum, cnt = 0, 0
	index_dict = {}
	for idx, value in enumerate(skills):
		index_dict[value] = idx

	while cnt != len(skills) - k + 1:
		target = sum(skills[cnt:cnt + k])  # 합
		if index_dict[value]

		# for idx in team:
		# 	if idx in index_list[cnt:cnt+k]:
		# 		check+=1

		if target >= maximum:
			maximum = target
		cnt += 1

	return maximum

print("answer: ", solution(skills, team, k))




