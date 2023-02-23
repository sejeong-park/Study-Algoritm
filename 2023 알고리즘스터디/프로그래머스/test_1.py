# 시간 단위 바꾸기
def change_time(time) :
    h, m = time.split(':')
    return int(h) * 60 + int(m)

def solution(bakery_schedule, current_time, k):
    answer = -2

    now = change_time(current_time)
    bread, end_time = 0,0

    for schedule in bakery_schedule :
        time, n = schedule.split()
        time = change_time(time)
        if time >= now :
            bread += int(n)
        if bread >= k:
            end_time = time
            break

    answer = end_time - now

    if answer >= 0:
        return answer
    else:
        return -1