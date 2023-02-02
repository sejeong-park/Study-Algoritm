# 정렬 유형을 정리햅자

# 거품 정렬
def BubbleSort(x) :
	"""
	배열의 끝에 가장 큰 값을 배치 시키는 알고리즘
	인접한 두 원소를 비교하여, 스왑하는 것을 반복
	"""
	for i in range(len(x)-1,0,-1) :
		for j in range(i) :
			if x[j] > x[j+1] :
				x[j], x[j+1] = x[j+1], x[j]  # swap
	return x

# 퀵 정렬
def QuickSort_1(x) :
	"""
	기준이 되는 pivot을 잡고, 재귀적으로 실행하여, 기준값 전후로 크기를 재배치한다.
	"""
	if len(x) <= 1:
		return x
	pivot = x[len(x)//2]	# 기준 점
	left, right, equal = [],[], []
	for i in x:
		if i < pivot :
			left.append(i)
		elif i > pivot :
			right.append(i)
		else:
			equal.append(i)
	# 재귀로 반복
	return QuickSort_1(left) + equal + QuickSort_1(right)

def QuickSort_2(x) :
	"""
	파이썬의 장점을 살린 퀵정렬 소스코드
	"""
	if len(x) < 1:
		return x

	pivot, tail = x[0], x[1:] # 피벗은 첫번째 원소

	left_side = [x for x in tail if x <= pivot]
	right_side = [x for x in tail if x > pivot]

	return QuickSort_2(left_side) + [pivot] + QuickSort_2(right_side)

def insertionSort(x):
	"""
	차례대로 이미 정렬된 부분 배열과 비교하여,
	자신보다 큰 값과 작은 값 사이의 적당한 위치를 찾아 삽입
	"""
	for i in range(1, len(x)):
		# 인덱스 i부터 1씩 감소하며, 반복
		for j in range(i, 0, -1) :
			# 한 칸씩 왼쪽으로 이동
			if x[j] < x[j-1] :
				x[j], x[j-1] = x[j-1] , x[j]
			# 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
			else:
				break
	return x

def mergeSort(x):
	if len(x) < 2:
		return x

	mid = len(x) // 2
	left_side = mergeSort(x[:mid])
	right_side = mergeSort(x[mid:])

	merge_array = []
	left, right = 0,0

	while left < len(left_side) and right < len(right_side):
		if left_side[left] < right_side[right] :
			merge_array.append(left_side[left])
			left += 1
		else:
			merge_array.append(right_side[right])
			right += 1

	merge_array += left_side[left:]
	merge_array += right_side[right:]

	return merge_array

def countSort(x):
	count = [0] * (max(x) + 1)

	# 각 해당하는 인덱스의 값 증가
	for i in range(len(x)):
		count[x[i]] += 1
	output = []
	for i in range(len(count)) :
		for j in range(count[i]) :
			output.append(i)

	return output

input = ['apple', 'cat', 'fox', 'banana', 'spring', 'hello', 'world']
print(BubbleSort(input))
print(QuickSort_1(input))
print(insertionSort(input))
print(mergeSort(input))
count_input = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
print(countSort(count_input))