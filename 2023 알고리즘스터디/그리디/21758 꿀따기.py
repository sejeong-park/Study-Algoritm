# 21758 - 꿀따기
import copy
n = int(input())
array = list(map(int, input().split()))
table = copy.deepcopy(array)

maxCnt = 0

# 0. 누적합의 테이블 구하기 (array의 합한 값 table 미리 구하기)
for i in range(1, n):
	table[i] += table[i-1]

# print(table)
# # [9, 18, 22, 23, 27, 36, 45]


# 벌(1) - 벌(2) - 꿀
for i in range(1, n-1) :
	maxCnt = max(maxCnt, 2 * table[-1] - array[0] - array[i] - table[i])

# 꿀 - 벌(1) - 벌(2)
for i in range(1, n-1) :
	# 2번 벌이 먹을 수 있는 크기 : table[-1] - array[-1] - array[i] (2번 벌은 오른쪽 마지막)
	# 1번 벌이 먹을 수 있는 크기 :
	maxCnt = max(maxCnt, (table[-1] - array[-1] - array[i]) + (table[i-1]))

# 벌(1) - 꿀 - 벌(2)
for i in range(1, n-1) :
	# i 는 꿀통의 위치
	maxCnt = max(maxCnt, (table[i] - array[0]) + (table[-1] - table[i-1] - array[-1]))
print(maxCnt)