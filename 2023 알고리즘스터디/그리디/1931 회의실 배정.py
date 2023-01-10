# 1931 회의실 배정

n = int(input())
timelists = []
for _ in range(n):
	timelists.append(tuple(map(int, input().split())))

timelists.sort(key = lambda x : (x[1], x[0]))

print(timelists)
cnt = 0
last_time = 0
for start, end in timelists:
	if start >= last_time:
		cnt += 1
		last_time = end


print(cnt)