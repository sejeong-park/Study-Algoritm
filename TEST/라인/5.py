from typing import List
fees = [[4,1000],[6,1000],[21,3000],[16,2000],[26,3000]]
t = 27
def solution(fees: List[List[int]], t: int) -> List[int]:
    answer = []

    for idx, fee in enumerate(fees):
        result = 0
        a, b = fee
        for idx in range(t//a):
            update_fee = b + idx * b
            result += update_fee
        print(result)

        print('---')


    return answer


print(solution(fees, t))