# 조합
def solution(number, k):
    answer = ""
    stack = []
    for num in number:
        while stack and stack[-1]<num and k>0:
            k-=1

            stack.pop()
        stack.append(num)
        print(stack)
    return "".join(stack[:len(stack)-k])

print(solution('4177252841',4))