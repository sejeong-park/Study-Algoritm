# 소프티어 성적평가

import sys

n = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]
final = [0] * (n)

for score in scores:
	result = []
	for i in range(n):
		rank = 1
		final[i] += score[i]
		for j in range(n):
			if score[i] < score[j] :
				rank += 1
		result.append(rank)
	print(*result)

final_rank = []
for i in range(n):
	rank = 1
	for j in range(n) :
		if final[i] < final[j] :
			rank += 1
	final_rank.append(rank)
print(*final_rank)
