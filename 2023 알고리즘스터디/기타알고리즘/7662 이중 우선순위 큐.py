# 7662 이중 우선순위 큐
import heapq
t = int(input())
for _ in range(t):
	k = int(input())
	max_queue = []
	min_queue = []
	visited = [False] * k
	for i in range(k):
		key, value = map(str, input().split())
		if key == 'I' :
			heapq.heappush(min_queue, (int(value), i))
			heapq.heappush(max_queue, (- int(value), i))
			visited[i] = True
		elif key == 'D' :
			# 최대 값 삭제
			if int(value) == 1:
				# 반복문을 통해, 이미 제거된 정수는 pop하여 제거
				while max_queue and visited[max_queue[0][1]] == False:
					heapq.heappop(max_queue)
				# 최대 힙이 있으면 최대 힙 제거
				if max_queue:
					visited[max_queue[0][1]] = False
					heapq.heappop(max_queue)
			elif int(value) == -1:
				# 반복문을 통해, 이미 제거된 정수는 pop 하여 제거
				while min_queue and visited[min_queue[0][1]] == False:
					heapq.heappop(min_queue)
				if min_queue:
					visited[min_queue[0][1]] = False
					heapq.heappop(min_queue)


	while min_queue and not visited[min_queue[0][1]]:
		heapq.heappop(min_queue)
	while max_queue and not visited[max_queue[0][1]]:
		heapq.heappop(max_queue)

	if not min_queue or not max_queue:
		print("EMPTY")
	else:
		print(-max_queue[0][0], min_queue[0][0])