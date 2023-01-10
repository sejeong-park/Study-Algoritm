n = int(input())
timelists = []
for _ in range(n):
	timelist = tuple(map(int, input().split()))
	timelists.append(timelist)

# 종료 시간을 기준으로 오름차순 해주기
timelists.sort(key = lambda x: (x[1], x[0]))

cnt = 0
last_time = 0
for start, end in timelists:
	# start가 마지막 시간보다 크면 새로운 반에 배정
	if start >= last_time:
		cnt += 1
		last_time = end

print(cnt)