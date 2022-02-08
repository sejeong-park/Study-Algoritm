n, m = map(int, input().split())
rice_cake = list(map(int,input().split()))

start = 0
end = max(rice_cake)
result =0
while(start<=end):
    total = 0
    mid = (start + end)//2
    for cake in rice_cake:
        # 잘랐을 때 떡의 양 갱신
        if cake>mid:
            total += cake - mid

    # 떡의 양이 부족한 경우 더 많이 자르도록
    if total<m:
        end = mid-1
    else:
        result = mid    # 최대한 덜 잘랐을 때가 정답 -> 여기서 result를 기록
        start = mid+1

print(result)