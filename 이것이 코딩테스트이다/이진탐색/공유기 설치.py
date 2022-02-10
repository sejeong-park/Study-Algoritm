# 집의 개수(N)과 공유기의 개수(C) 입력받기
n, c = list(map(int, input().split()))

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
    array.append(int(input()))
array.sort()        # 이진 탐색 수행을 위해 정렬 수행

start = array[1]-array[0]
end = array[-1] - array[0]

#print(start, end)
result = 0
while(start<=end):
    mid = (start + end)//2      # mid 는 가장 인접한 두 공유기 사이의 거리를 의미
    value = array[0]
    count = 1

    for i in range(1,n):
        if array[i] >= value+mid:
            value = array[i]
            count+=1
    if count>=c:
        start = mid+1
        result = mid    # 최적의 결과를 저장
    else:
        end = mid-1

print(result)
