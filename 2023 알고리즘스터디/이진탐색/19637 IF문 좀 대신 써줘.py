# 19637 IF문 좀 대신 써줘
import sys
import bisect
input = sys.stdin.readline # 입력데이터가 많을 수 있기 때문
n, m = map(int, input().split())
power_list = []
name_list = []
for _ in range(n):
	name, power = input().split()
	power_list.append(int(power))
	name_list.append(name)

for _ in range(m):
	target = int(input())
	index = bisect.bisect_left(power_list, target)
	print(name_list[index])
