# 카카오 20년 인턴 기출 - 후보키 -> 모르겠다..
from itertools import combinations
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# 모든 경우의 수를 만든 후 유일성, 최소성을 만족하지 않는 부분은 제거
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    # 전체 조합
    candidates = []
    for i in range(1, col + 1):
        candidates.extend(combinations(range(col), i))
    print(candidates)

    #유일성
    unique = []
    for candidate in candidates:
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        if len(set(tmp)) == row:
            unique.append(candidate)

    print(unique)

    # 최소성
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])
    print(answer)
    return len(answer)

print(solution(relation))
