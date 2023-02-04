# 11660 - 구간합 구하기 5

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
table = [[0] * (n+1) for _ in range(n+1)]

# 누적합 테이블 만들기
for row in range(1, n+1):
	for col in range(1, n+1):
		table[row][col] = table[row][col-1] + table[row-1][col] - table[row-1][col-1] + array[row-1][col-1]
# print(table)

for _ in range(m):
	x1, y1, x2, y2 = map(int, input().split())
	print(table[x2][y2] - table[x1-1][y2] - table[x2][y1-1] + table[x1-1][y1-1] )


