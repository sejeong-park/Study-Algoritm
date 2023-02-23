def find_parent(p, idx) :
    if p[idx] != idx :
        p[idx] = find_parent(p, p[idx])
    return p[idx]

def solution(p, b):
    answer = []
    for idx, boss in enumerate(p):
        if p[idx] == -1 :
            p[idx] = idx
    for idx, boss in enumerate(p) :
        if p[idx] != idx :
            find_parent(p, idx)

    for target in b:
        # 자기 자신이 아닐경우
        if target != p[target] :
            answer.append(0)
        else:
            answer.append(p.count(target))

    return answer