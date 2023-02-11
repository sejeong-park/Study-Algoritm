test_case1 = [[2,0], [3,1]]
test_case2 = [[1,4,3], [1,2,2]]
test_case3 = [[0,2,0,1], [0,1,0,1]]

def solution(queries):

	for query in queries:
		for i in range(len(query)):
			if query[i] != 0 and query[i] - 1:
				
				print(query)

	return


print(solution(test_case1))
print()
print(solution(test_case2))
print()
print(solution(test_case3))