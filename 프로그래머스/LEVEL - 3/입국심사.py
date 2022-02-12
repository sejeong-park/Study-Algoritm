#       입국 심사
n = 6
times = [7,10]
def solutions(n, times):
    answer =0

    start = 1
    end = max(times)*n

    while (start<=end):
        mid = (start+end)//2
        total =0
        for time in times:
            total += mid//time

        if total>=n:
            answer = mid
            end = mid -1
        elif total<n:
            start = mid+1

    return answer

print(solutions(n, times))