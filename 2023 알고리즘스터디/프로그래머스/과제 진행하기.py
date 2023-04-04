from collections import deque
import copy


def change_time(time):
	hour, minuate = time.split(':')
	return int(hour) * 60 + int(minuate)


def solution(plans):
	answer = []
	# plans -> name, start, playtime
	stop = []

	plans.sort(key=lambda x: (x[1], x[2]))  # 시작 시간을 기준으로 정렬

	for idx in range(len(plans)):
		name, start, playtime = plans[idx]
		start_time, playtime = change_time(start), int(playtime)
		# 마지막이 아닐 경우
		if idx != len(plans) - 1:
			next_start_time = change_time(plans[idx + 1][1])  # 다음 타임

			if start_time + playtime <= next_start_time:
				answer.append(name)
				if stop:
					tmp = copy.deepcopy(stop)
					remain_time = next_start_time - (start_time + playtime)
					# 가장 최신인 마지막 부터
					for i in range(len(stop) - 1, -1, -1):
						if stop[i][1] <= remain_time:
							remain_time -= stop[i][1]  # 남은 시간 빼주기
							answer.append(stop[i][0])
							tmp.pop()
						else:
							tmp[-1][1] = stop[i][1] - remain_time
							break
					stop = copy.deepcopy(tmp)

			else:
				stop.append([name, start_time + playtime - next_start_time])
		else:
			answer.append(name)

	# 최신순반대대로
	for i in range(len(stop) - 1, -1, -1):
		answer.append(stop[i][0])

	return answer