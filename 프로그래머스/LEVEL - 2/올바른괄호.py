# 프로그래머스 - 올바른 괄호

def solution(s):
	answer = True

	start_tag = []
	end_tag = []

	# stack에 태그 넣기
	for idx, tag in enumerate(s):
		if tag == '(':
			start_tag.append(idx)
		else:
			end_tag.append(idx)

	if len(start_tag) != len(end_tag):
		return False

	for start, end in zip(start_tag, end_tag):
		if end < start:  # end에 들어간 index가 start의 index보다 작으면
			return False

	return True


s = "(()("
print(solution(s))