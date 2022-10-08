from datetime import datetime, timedelta

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today,terms, privacies) :
	answer = []
	term_dict = dict()
	today_y, today_m , today_d = today.split('.')

	for term in terms:
		term_type, month = term.split()
		term_dict[term_type] = int(month) * 28
	print(term_dict)
	for index, privacie in enumerate(privacies):
		start, term_type = privacie.split()
		start_y, start_m, start_d = start.split('.')

		result_y, result_m, result_d = int(today_y)-int(start_y) , int(today_m) - int(start_m) , int(today_d) - int(start_d)
		result_days = (12*result_y + result_m) * 28 + result_d
		print(result_days)
		if result_days >= term_dict[term_type]:
			answer.append(index+1)

	return answer

print(solution(today, terms, privacies))