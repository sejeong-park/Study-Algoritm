# 20551 - Sort 마스터 배지훈의 후계자
import sys
input = sys.stdin.readline	# 시간 초과

n, m = map(int, input().split())
array_B = sorted([int(input()) for _ in range(n)])
array_D = [int(input()) for _ in range(m)]

array_dict = dict()
for index, key in enumerate(array_B):
	if key not in array_dict:
		array_dict[key] = index

for D in array_D :
	print(array_dict[D] if D in array_dict else -1)
