import sys

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()

### 내풀이 -> 백준으로 50점 밖에 나오지 않음
# def check(n):
#     p = "I"
#     for _ in range(n):
#         p+="OI"
#     return p
#
# p = check(n)
# cnt = 0
# for idx in range(m):
#     if s[idx:idx+len(p)] == p:
#         cnt+=1
#     else:
#         continue
#
# print(cnt)


# 다른 블로그 참고한 것
idx, cnt, ans = 1,0,0
while idx <m-1:
    if s[idx-1] == 'I' and s[idx] == 'O' and s[idx+1] == 'I':
        cnt+=1
        if cnt == n:
            cnt-=1
            ans+=1
        idx+=1
    else:
        cnt = 0
    idx+=1

print(ans)


