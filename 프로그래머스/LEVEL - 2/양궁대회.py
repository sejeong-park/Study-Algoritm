from itertools import combinations

from itertools import combinations_with_replacement

"""
모르겠음 -> 일단 조합으로 때려보자. -> 중복 조합 (combinations_with_replacement)
"""


def solution(n, info):
	answer = [-1]
	# 중복 조합 케이스 - 과녁을 맞추자
	cases = list(combinations_with_replacement(range(10, -1, -1), n))
	max_distance = int(1e9)  # 점수 차
	for case in cases:

		# 어피치와 라이언 획득하는 점수
		apeach, lion = 0, 0
		info2 = [0] * 11  # 0 ~ 10

		for point in case:
			info2[point] += 1

		# index는 점수 (근데 0~10이면 뒤집어서 말해줘야됌) / cnt는 화살 개수
		for index, (apeach_cnt, lion_cnt) in enumerate(zip(info, info2)):
			if apeach_cnt > lion_cnt:
				apeach += 10 - index
			elif apeach_cnt < lion_cnt:
				lion += 10 - index
			else:
				# 점수가 같을 경우 어디도 가져가지 않는다.
				continue

		# 라이언이 우승해야함
		if lion > apeach:
			print(lion, apeach)
			distance = lion - apeach  # lion과 apeach의 점수 차
			if distance > max_distance:
				# 만약 점수차를 갱신하면 ?
				max_distance = distance  # 갱신
				answer = info2

	return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))