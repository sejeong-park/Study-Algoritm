# 1로 만들기
# DP 문제
n = int(input())
d = [0]*30001

for i in range(2,n+1):
    # 1을 더하는 이유는 d는 결과가 아닌, 계산한 횟수를 저장하는 것이기 때문
    d[i] = d[i-1]+1

    if i%2==0:
        d[i] = min(d[i],d[i//2]+1)
    if i%3 == 0:
        d[i] = min(d[i],d[i//3]+1)

print(d[n])