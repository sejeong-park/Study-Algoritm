# 메뉴 리뉴얼 - 조합

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

# ["AC", "ACDE", "BCFG", "CDE"]


from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []
    for k in course: # 횟수
        case = []
        for order in orders:
            for menu in combinations(order, k):
                result = ''.join(sorted(menu)) # sorted하는 이유 -> AC와 CA는 똑같기 때문
                case.append(result)
        #print("case::", case)
        sorted_case = Counter(case).most_common()
        #print("sorted_case :: ", sorted_case)

        result_map = {}
        for key, value in sorted_case:
            if len(key) not in result_map.keys() or result_map[len(key)] == value:
                if value <= 1:
                    break
                answer.append(''.join(key))
                result_map[len(key)] = value
        #print(result_map)
    return sorted(answer)

print(solution(orders, course))