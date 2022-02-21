# 기타 레슨
import sys
n, m =map(int, input().split())
array = list(map(int, input().split()))
start, end = max(array), sum(array)
answer = sys.maxsize
while(start<=end):
    mid = (start+end)//2
    cnt, sum = 0,0
    for idx in range(len(array)):
        if sum+array[idx]>mid:
            cnt+=1
            sum=0
        sum+=array[idx]
    if sum:
        cnt+=1
    if cnt>m:
        start = mid +1
    else:
        answer = min(answer, mid)
        end = mid-1

print(answer)