# 프로그래머스 고득점 키트 - 주식가격

prices = [1,2,3,2,3]

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for index, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            jdx = stack.pop()
            answer[jdx] = index - jdx
        stack.append(index)
        print(stack)
    print("answer : ", answer)
    while stack:
        jdx = stack.pop()
        answer[jdx] = len(prices) - 1 - jdx
    return answer

print(solution(prices))