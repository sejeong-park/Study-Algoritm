scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
def solution(scores) :
	new_list = list(map(list, zip(*scores))) # 세로로

	for i in range(len(scores)) :
		if new_list[i].count(new_list[i][i]) == 1 and (new_list[i][i] == max(new_list[i])) :
			del new_list[i][i]

		mean = sum(new_list[i]) / len(new_list[i])
		if mean >= 90 :
			new_list[i] = 'A'
		elif 80 <= mean < 90 :
			new_list[i] = 'B'
		elif 70 <= mean < 80 :
			new_list[i] = 'C'
		elif 50 <= mean < 70 :
			new_list[i] = 'D'
		elif mean < 50 :
			new_list[i] = 'F'
	return ''.join(new_list)
print(solution(scores))