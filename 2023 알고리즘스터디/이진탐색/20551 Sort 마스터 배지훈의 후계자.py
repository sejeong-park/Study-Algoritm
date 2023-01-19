# 20551 Sort 마스터 배지훈의 후계자
import sys
input = sys.stdin.readline # 시간초과 나서, 첨부한 것
n, m = map(int, input().split())
array_B = sorted([int(input()) for _ in range(n)])

def binary_search(array, target):
	"""
	lower bound 적용된 binary_serach
	lower_bound란 찾고자 하는 값이 가장 처음으로 나오는 위치를 찾는 함수
	[-1,1,3,3,3,4,5,6,6]
	정답은 3의 인덱스는 2인데, 3의 인덱스가 5인채로 out 되는 경우 존재
	end = mid를 해주어, while문을 벗어날때까지 end의 값을 하나씩 줄여준다.
	-> 가장 먼저 등장하는 인덱스를 찾을 수 있도록
	"""
	start, end = 0, n-1
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			if end == mid:	# lower_bound -> end와 mid가 같을 때, 중단
				break
			end = mid	# while 문을 벗어날때까지 mid-1

		# 중간점보다 타겟이 더 작은경우
		elif array[mid]	> target:
			end = mid-1

		# 중간점보다 타겟이 더 큰 경우
		elif array[mid] < target:
			start = mid+1

	if array[mid] == target:
		return mid
	else:
		return -1

for _ in range(m):
	D = int(input())
	print(binary_search(array_B, D))



