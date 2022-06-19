
periods = [20,23,24]
payments = [[100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
            [100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000,100000],
            [350000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000,50000]]
estimates = [100000,100000,100000]

def solution(periods, payments, estimates):
    answer = []
    cnt1, cnt2 = 0,0
    this_vip = [False, False, False]
    next_vip = [False, False, False]

    for idx in range(3):
        total_payments = sum(payments[idx])
        next_month = periods[idx] + 1
        next_total_payments = sum(payments[idx][1:]) + estimates[idx]
        print(next_total_payments)
        if total_payments>=900000:
            if 24<=periods[idx]<60:
                this_vip[idx] = True

        elif 600000 <= total_payments < 900000:
            if 60<=periods[idx]:
                this_vip[idx] = True

        if next_total_payments >= 900000:
            if 24 <= next_month < 60:
                next_vip[idx] = True

        elif 600000 <= next_total_payments < 900000:
            if 60 <= next_month:
                next_vip[idx] = True
    print(this_vip)
    print(next_vip)
    for this, next in zip(this_vip, next_vip):
        if not this and next:
            cnt1 += 1
        if this and not next:
            cnt2 += 1


    answer = [cnt1, cnt2]
    return answer

print(solution(periods, payments, estimates))



