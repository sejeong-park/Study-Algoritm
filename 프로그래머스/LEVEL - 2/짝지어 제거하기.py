def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if s[i] == stack[-1]:   # stack의 마지막 값과 s[i]의 값이 같으면 pop()
                stack.pop()
            else:
                stack.append(s[i])  # stack의 마지막 값과 s[i]의 값이 다르면 push()


    if stack:   # 스택이 비어있지 않다면 0으로 리턴
        return 0
    else:       # 스택이 비어 있다면 1로 리턴
        return 1


    return answer

print(solution('baabaa'))