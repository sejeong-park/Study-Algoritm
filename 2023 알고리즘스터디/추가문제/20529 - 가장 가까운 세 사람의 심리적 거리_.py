# 20529 - 가장 가까운 세 사람의 심리적 거리
from itertools import combinations

def total_distance(a, b, c):
	cnt = 0
	for i in range(4):
		if a[i] != b[i]:
			cnt += 1
		if b[i] != c[i]:
			cnt += 1
		if a[i] != c[i]:
			cnt += 1
	return cnt

t = int(input())
for _ in range(t):
	n = int(input())
	mbti_list = list(map(str, input().split()))
	# 비둘기 집 원리 : (n+1)개의 물건을 n개의 상자에 넣을 때, 적어도 어느 한 상자에는 두 개 이상의 물건이 들어 있다는 원리
	# 16가지 MBTI가 있을 때 n>16이면, 이 중 같은 mbti를 가지는 사람은 반드시 두 명 이상이다.
	# k>32이면 같은 MBTI를 가지는 사람이 반드시 세 명 이상 있다는 것
	# 따라서 32이상이면 답은 0
	if n>32:
		print(0)
	else:
		min_distance = 100
		for i in range(0,n-2):
			for j in range(i+1, n-1):
				for k in range(j+1, n):
					min_distance = min(min_distance, total_distance(mbti_list[i], mbti_list[j], mbti_list[k]))
		print(min_distance)
