# 11000 - 강의실 배정
import heapq

n = int(input())
queue = []
for idx in range(n):
	s, e = map(int, input().split())
	queue.append([s, e])
queue.sort()

# print(queue)
# 방에 입력 시작
room = []
heapq.heappush(room, queue[0][1])

for i in range(1, n):
	# 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 더 빠르면
	if queue[i][0] < room[0] :
		heapq.heappush(room, queue[i][1])	# 새로운 회의실 개설
	else:
		heapq.heappop(room)			# 새로운 회의로 시간 변경을 위해 pop 후 새시간 push
		heapq.heappush(room, queue[i][1])

print(len(room))