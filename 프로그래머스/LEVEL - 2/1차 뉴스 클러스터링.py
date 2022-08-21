# 프로그래머스 - 1차 뉴스 클러스터링
import re

str1 = "handshake"
str2 = "shake hands"


def make_list(sentence):
	str_list = []
	for idx in range(len(sentence) - 1):
		# 영어일 때만
		if sentence[idx].isalpha() and sentence[idx + 1].isalpha():
			str_list.append(sentence[idx: idx + 2])

	return str_list


def solution(str1, str2):
	answer = 0

	str1_list = make_list(str1.lower())
	str2_list = make_list(str2.lower())

	intersection_list = set(str1_list) & set(str2_list)
	union_list = set(str1_list) | set(str2_list)
	if len(union_list) == 0:  # 공집합일때 고려
		return 65536

	# 유사도
	inter_len = sum([min(list(str1_list).count(intersection), list(str2_list).count(intersection)) for intersection in
					 intersection_list])
	union_len = sum([max(list(str1_list).count(union), list(str2_list).count(union)) for union in union_list])

	answer = int(65536 * inter_len / union_len)

	return answer


print(solution(str1, str2))