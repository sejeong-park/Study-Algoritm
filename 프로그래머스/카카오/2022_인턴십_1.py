

survey = ["TR", "RT", "TR"]
choices  = [7,1,3]

cases = [['R','T'],['C','F'],['J','M'],['A','N']]
type_list = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
score_list = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
def solutions(survey, choices):
    answer = ""
    for idx in range(len(choices)):
        survey_idx, score = survey[idx], choices[idx]
        if score<=3:
             type_list[survey_idx[0]] += score_list[score]
        elif score>=5:
            type_list[survey_idx[1]] += score_list[score]
    print(type_list)


    for case in cases:
        if type_list[case[0]] > type_list[case[1]]:
            answer += case[0]
        elif type_list[case[0]] < type_list[case[1]]:
            answer += case[1]
        else:
            answer += sorted(case)[0]


    return answer
print(solutions(survey,choices))