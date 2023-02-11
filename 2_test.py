test_case1 = [".....####",'..#...###', '.#.##..##'
			  , '..#..#...', '..#...#..', '...###...']	# 26
test_case2 = ['.#.','#..', '.#.'] # 3
test_case3 = ['####','##.#', '.#.#'] # 9
from collections import deque


def bfs(ox, oy, grid, visited):
	n , m = len(visited), len(visited[0])
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	queue = deque([(ox,oy)])
	visited[ox][oy] = True
	cnt = 1
	while queue:
		x, y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]
			if 0<=nx<n and 0<=ny<m and not visited[nx][ny] :
				if grid[nx][ny] == '.':
					queue.append((nx, ny))
					visited[nx][ny] = True
					cnt += 1
	return cnt, visited

def solution(grid):
	n, m = len(grid), len(grid[0])
	visited = [[False] * m for _ in range(n)]
	total = 0

	points = []
	for i in range(0,n):
		points.append((i,0))
		points.append((i,m-1))
	for i in range(0, m):
		points.append((0,i))
		points.append((n-1,i))

	for point in points:
		x, y = point
		if grid[x][y] == '.' and not visited[x][y]:
			cnt, visited = bfs(x, y, grid, visited)
			total += cnt

	return n*m - total

print(solution(test_case1)) # 26
print(solution(test_case2)) # 3
print(solution(test_case3))	# 9
