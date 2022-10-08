p = [2,5,3,1,4]

def solution(p):
    answer = [0]*len(p)
    for idx in range(len(p)):
        tmp_list = p[idx:]
        tmp_min = min(tmp_list)
        tmp_min_index = tmp_list.index(tmp_min)
        if idx != idx + tmp_min_index:
            p[idx], p[idx + tmp_min_index] = p[idx + tmp_min_index],p[idx]
        print(p)
    return answer

print(solution(p))


