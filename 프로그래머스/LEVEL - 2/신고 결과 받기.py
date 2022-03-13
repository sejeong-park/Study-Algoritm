# 시간복잡도 때문에 불통!!!
def solution(id_list, report, k):
    answer = []

    report_list = dict()
    black_list = dict()

    # 1. 누가 누구에게 신고했는지 report_list에 기록
    for user in report:
        report_user, target_user = user.split(' ')
        # 제보한 사람이 report_list에 없으면 리스트 추가
        if report_user not in report_list:
            report_list[report_user] = []

        # 제보 받은 사람이 제보한 사람의 리스트에 있으면 1회만 가능 (중복 신고 불가능)
        if target_user not in report_list[report_user]:
            report_list[report_user].append(target_user)


    #print(report_list)

    # 2. 신고받은 사람들의 리스트를 따로 만들어 신고 받은 횟수 카운트
    for report_idx in report_list.values():
        for black_user in report_idx:
            if black_user not in black_list:
                black_list[black_user] = 1
            else:
                black_list[black_user] +=1
    #print(black_list)

    # 3. k번 이상 신고 받은 사람들 리스트를 따로 만들어 관리
    stop_user = []
    for user, cnt in black_list.items():
        if cnt >= k:
            stop_user.append(user)
    #print(stop_user)

    # 4. 정지 리스트에 없는 회원은 report_list에서 제외해줌
    for key_user, value_user in report_list.items():
        for user in value_user:
            if user not in stop_user:
                value_user.remove(user)
    #print(report_list)

    # 5. 만약 id리스트의 id가 report_list에 있으면 report_list의 len값을 주고, 아니면 0 채우기
    for id in id_list:
        if id in report_list.keys():
            answer.append(len(report_list[id]))
        else:
            answer.append(0)



    return answer

id_list = ["muzi",'frodo','apeach','neo']
report = ["muzi frodo","apeach frodo", "frodo neo", "muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k=3
print(solution(id_list, report, k))