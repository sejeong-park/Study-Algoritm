# 19598 최소 회의실 개수

n = int(input())
timeline = []
for _ in range(n):
	start, end = map(int, input().split())
	timeline.append([start, 1])
	timeline.append([end, -1])

timeline.sort()

cnt = 0
room = 0
for time, state in timeline:
	cnt += state
	room = max(cnt, room)

print(room)