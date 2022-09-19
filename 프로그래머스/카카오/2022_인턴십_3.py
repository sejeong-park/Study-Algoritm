d#
alp = 10
cop = 10
problems = [[10,15,2,1,2],[20,20,3,3,4]]
def solution(alp, cop, problems):
    answer = 0
    total_time = 0
    for problem_idx, problem in enumerate(problems):
        if problem_idx-1 < 0 or cost<time:
            if alp<alp_req:


        problems.sort() # 이거 나중에 가능여부를 지워줄거!!
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        # 다음문제에서 조건 모자랄때
        if alp < alp_req:
            total_time += alp_req - alp
        if cop < cop_req:
            total_time += cop_req - cop
        # 다른 조건 통과했을 때,
        else:

    print(problems)

    return answer
print(solution(alp,cop, problems))