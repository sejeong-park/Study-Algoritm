import sys
input = sys.stdin.readline
# rstip은 sys.stdin.readline 만 써주면 줄바꿈 문자도 들어가게 됨
n,m = map(int,input().split())
poketmon = dict()
for idx in range(n):
    name = input().rstrip()
    poketmon[idx+1] = name
    poketmon[name] = idx+1

for _ in range(m):
    quiz = input().rstrip()
    if quiz.isdigit()==True:
        print(poketmon[int(quiz)])
    else:
        print(poketmon[quiz])
