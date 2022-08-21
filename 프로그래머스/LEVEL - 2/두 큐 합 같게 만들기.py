# 프로그래머스 - 두 큐 합 같게 만들기

from collections import deque

queue1 = [1, 1]
queue2 = [1, 5]


def solution(queue1, queue2):
	answer = 0  # == cnt
	size = len(queue1)  # 값이 일치하지 않을 때 무한대로 반복됨을 방지
	queue1_sum = sum(queue1)
	queue2_sum = sum(queue2)

	queue1 = deque(queue1)
	queue2 = deque(queue2)

	if queue1_sum == queue2_sum:
		return answer

	while queue1_sum != queue2_sum and answer <= 3 * size:

		if queue1_sum < queue2_sum:
			tmp = queue2.popleft()
			queue1.append(tmp)
			queue2_sum -= tmp
			queue1_sum += tmp
		else:
			tmp = queue1.popleft()
			queue2.append(tmp)
			queue1_sum -= tmp
			queue2_sum += tmp
		answer += 1

	if queue1_sum != queue2_sum:
		return -1

	return answer


print(solution(queue1, queue2))