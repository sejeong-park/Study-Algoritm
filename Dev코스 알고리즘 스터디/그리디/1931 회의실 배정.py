# 주유소

n = int(input())
timetable = []
for _ in range(n) :
	s, e = map(int, input().split())
	timetable.append((s, e))

timetable.sort(key = lambda x : (x[1], x[0]))

cnt = 0
check = 0 # 마지막 시간 체크하기
for s, e in timetable :
	if s >= check :
		cnt += 1
		check = e

print(cnt)
