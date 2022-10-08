# 15686 - 치킨 배달
from itertools import permutations, combinations
n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
chicken_list = []
house_list = []

for i in range(n):
	for j in range(n):
		if array[i][j] == 2:
			chicken_list.append((i,j))
		elif array[i][j] == 1:
			house_list.append((i,j))

result = 1e9
for chicken in combinations(chicken_list, m):
	chicken_distance = 0
	for house in house_list:
		# 집과 치킨 집의 최소 거리
		distance = [abs(house[0] - chick[0]) + abs(house[1] - chick[1]) for chick in chicken]
		chicken_distance += min(distance)
	result = min(result, chicken_distance)

print(result)
