# 20529 - 가장 가까운 세 사람의 심리적 거리 # 시간초과 풀ㅇ

from itertools import combinations
import time
start = time.time()
t = int(input())

for _ in range(t) :
	n = int(input())
	mbti_list = list(map(str, input().split()))
	test1 = time.time()
	mbti_list = list(combinations(mbti_list, 3))
	test2 = time.time()
	print(test2-test1)
	# print(mbti_list)
	target_list = []
	for group in mbti_list:
		a,b,c = group
		cnt = 0
		for i in range(4):
			if a[i] != b[i]:
				cnt += 1
			if a[i] != c[i]:
				cnt += 1
			if b[i] != c[i]:
				cnt += 1
		target_list.append((a,b,c,cnt))

	target_list.sort(key = lambda x : x[3])
	print(target_list[0][3])

end = time.time()
print(end - start)

