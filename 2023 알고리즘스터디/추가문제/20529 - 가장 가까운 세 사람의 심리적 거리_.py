# 20529 - 가장 가까운 세 사람의 심리적 거리
from itertools import combinations

def distance(a, b):
	cnt = 0
	for i in range(4):
		if a[i] != b[i]:
			cnt += 1
	return cnt

t = int(input())
for _ in range(t):
	n = int(input())
	mbti_list = list(map(str, input().split()))

	if n>32:
		print(0)
	else:
		min_distance = 100
		for i in range(0,n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					total_distance = distance(mbti_list[i], mbti_list[j]) + distance(mbti_list[j], mbti_list[k]) + distance(mbti_list[i], mbti_list[k])
					min_distance = min(min_distance, total_distance)
		print(min_distance)

