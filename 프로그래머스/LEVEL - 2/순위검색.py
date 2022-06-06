import sys

from itertools import combinations
from collections import defaultdict

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

def solution(info, query):
    answer = []
    infos = defaultdict(list)

    for i in info:
        conditions = i.split()[:-1]
        score = int(i.split()[-1])

        for r in range(5):
            combis = list(combinations(range(4),r)) # '-'로 바꿀 경우의 수를 추출

            for c in combis:
                test_cases = conditions[:]
                for v in c:
                    test_cases[v] = '-'
                infos['_'.join(test_cases)].append(score)

    for item in infos:
        infos[item].sort()

    for q in query:
        q = q.replace('and','').split()
        conditions = '_'.join(q[:-1])
        score = int(q[-1])

        if conditions in list(infos):
            data = infos[conditions]
            if len(data) > 0:
                start, end = 0, len(data)
                while start != end and start != len(data):
                    if data[(start + end)//2] >= score:
                        end = (start + end)//2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(data)-start)
        else:
            answer.append(0)

    return answer


print(solution(info, query))