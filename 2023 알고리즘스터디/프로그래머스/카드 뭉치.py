def solution(cards1, cards2, goal):
    answer = ''
    cnt = 0
    for keyword in goal :
        if cards1 and cards1[0] == keyword:
            cards1.remove(cards1[0])
            cnt += 1
        if cards2 and cards2[0] == keyword:
            cards2.remove(cards2[0])
            cnt += 1
    if cnt == len(goal):
        answer = "Yes"
    else:
        answer = "No"
    return answer