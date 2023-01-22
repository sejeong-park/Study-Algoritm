import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
stations = list(map(int, input().split()))
stations.append(0)
stations.append(L-1)
stations = sorted(stations)

left = 0
right = L-1
while left <= right:
    mid = (left+right) // 2

    print(stations, " mid = ", mid, end=' ')
    count = 0 # 설치한 휴게소의 수
    for i in range(1, len(stations)):
        if stations[i] - stations[i-1] > mid:
            count += (stations[i] - stations[i-1] -1)//mid
            print("count = ",count)
    if count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)