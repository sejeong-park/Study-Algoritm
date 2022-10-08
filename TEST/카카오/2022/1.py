from datetime import datetime, timedelta

today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

def solution(today,terms, privacies) :
	answer = []
	term_dict = dict()
	today = today.replace('.','-')
	today = datetime.strptime(today, "%Y-%m-%d")

	for term in terms:
		a,b = term.split()
		term_dict[a] = int(b)

	for privacie in privacies:
		start_time ,term_type = privacie.split()
		start_time = datetime.strptime(start_time.replace('.','-'), "%Y-%m-%d")
		#after_time = today + timedelta(month = term_dict[term_type])

		# 오늘날짜로부터 몇 Day 지났는 지 계산
		delta_day = today - start_time

		print(today - start_time)

	return answer

print(solution(today, terms, privacies))