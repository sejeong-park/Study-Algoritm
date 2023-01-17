# 2606 바이러스
from collections import deque

k = int(input())
n = int(input())

computer = {int(i+1) : [] for i in range(k)}

for _ in range(n) :
	a, b = map(int, input().split())
	computer[a].append(b)
	computer[b].append(a)

# 1번 컴퓨터가 바이러스에 걸렸을 때, 컴퓨터의 수
visited = [False for _ in range(k+1)]

queue = deque([1])
visited[1] = True
cnt = 0
while queue:
	key = queue.popleft()
	for i in computer[key]:
		if not visited[i]:
			queue.append(i)
			visited[i] = True
			cnt += 1

print(cnt)