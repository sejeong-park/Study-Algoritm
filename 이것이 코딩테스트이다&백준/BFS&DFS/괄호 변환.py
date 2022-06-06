# 제대로 된 괄호 문자열 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        else:
            count-=1

        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            # 쌍이 맞지 않는 경우에 False 반환
            if count == 0:
                return False
            count-=1
    return True


def solution(p):
    answer = ''
    # 입력 문자열이 공백이면, 그대로 반환
    if p == '':
        return answer

    index = balanced_index(p)
    print(index)
    u = p[:index+1]
    v = p[index+1:]
    print("u", u)
    print("v", v)
    # 올바른 괄호 문자열이면, v에 대해 함수를 수행한 결과를 붙여 반환

    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면, 아래 과정 수행
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

    return answer


print(solution("()))((()"))
