# JadenCase 문자열 만들기

s = "3people unFollowed me   hello 3948DDD 3948HelloD"

def solution(s) :

	s_list = s.split(" ")
	for idx,s_object in enumerate(s_list):
		s_object = s_object.capitalize()
		s_list[idx] = s_object
	return " ".join(s_list)

print(solution(s))