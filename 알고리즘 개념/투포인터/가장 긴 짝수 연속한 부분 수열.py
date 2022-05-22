# 가장 긴 짝수 연속한 부분 수열

n, k = map(int, input().split())
array = list(map(int, input().split()))
# 연속된 홀수를 따지면 됨

end = 0
result = 0
tmp = 0
count = 0

for start in range(n):
    # end 만큼 이동
    while count<=k and end<n:
        ## 홀수라면
        if array[end] % 2 == 1:
            count+=1
        else:
            tmp+=1
        end += 1 # 끝점 이동

        if start == 0 and end == n:
            result = tmp
            break

    if count == k+1:
        result = max(tmp, result)
    if array[start]%2 == 1:# 시작점이 홀수
        count -=1
    else:# 시작점이 짝수
        tmp -= 1

print(result)