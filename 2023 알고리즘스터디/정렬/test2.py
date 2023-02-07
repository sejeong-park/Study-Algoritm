

def sort_array(x):
	for i in range(len(x)):
		for j in range(i, 0, -1):
			if x[j] < x[j-1]:
				x[j] , x[j-1] = x[j-1] , x[j]

			else:
				break
	return x

input = [3,5,2,1,7,9]
print(sort_array(input))

from collections import deque

import sys

input = sys.stdin.readline

def radixSort(arr):
    buckets = [deque() for _ in range(10)]
    Q = deque(arr)
    cur = 1

    while max(arr) >= cur:

        while Q:
            num = Q.popleft()
            buckets[(num//cur)%10].append(num)

        for bucket in buckets:
            while bucket:
                Q.append(bucket.popleft())
        cur *= 10

    return list(Q)

arr = [12, 9, 1, 6, 5, 28]
print(arr)
print(radixSort(arr))