# 프로그래머스 - 탐욕법 - 그리디
# 투포인터 방식의 풀
people = [70,50,80,50]
limit = 100

def solution(people, limit):
	answer = 0

	people.sort()
	print(people)

	start, end = 0, len(people)-1
	while start <= end:
		answer += 1
		if people[start] + people[end] <= limit:
			start +=1
		end -= 1

	return answer
print(solution(people, limit))