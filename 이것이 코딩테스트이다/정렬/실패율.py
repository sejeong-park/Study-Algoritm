def solution(n, stages):
    answer = []
    stage_len = len(stages)
    result = []
    for stage in range(1, n+1):
        stage_cnt = stages.count(stage) #stages에 stage 몇 개인지 카운트
        result.append((stage, stage_cnt / stage_len))
        stage_len -= stage_cnt

    result.sort(key = lambda x:x[1], reverse = True)

    for stage, fail in result:
        answer.append(stage)
    return answer

n = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(n, stages))