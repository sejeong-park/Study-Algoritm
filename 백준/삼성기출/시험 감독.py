# 13458 - 시험 감독

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0
for size in a:
    if size>=b:
        size-=b
        if size%c == 0:
            answer += size//c
        else:
            answer += size//c+1

print(answer + n)