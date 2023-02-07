
# 1. 버블 정렬
def BubbleSort(x):
	for i in range(len(x)-1, 0 , -1):
		for j in range(i):
			if x[j] > x[j+1]:
				x[j], x[j+1] = x[j+1], x[j]
	return x

def QuickSort(x):
	if len(x)<=1:
		return x

	pivot, tail = x[0], x[1:]
	left_side = [i for i in tail if i <= pivot]
	right_side = [i for i in tail if i > pivot]

	return QuickSort(left_side) + [pivot] + QuickSort(right_side)

def insertionSort(x):
	for i in range(1, len(x)):
		for j in range(i, 0, -1):
			if x[j] < x[j-1] :
				x[j], x[j-1] = x[j-1], x[j]
			else:
				break

	return x

def mergeSort(x):
	if len(x) <= 1:
		return x

	mid = len(x) // 2
	left, right = 0,0
	left_side = mergeSort(x[:mid])
	right_side = mergeSort(x[mid:])

	merge_array = []

	while left < len(left_side) and right < len(right_side):
		if left_side[left] < right_side[right]:
			merge_array.append(left_side[left])
			left += 1

		else:
			merge_array.append(right_side[right])
			right += 1

	merge_array += left_side[left:]
	merge_array += right_side[right:]
	return merge_array


input = ['apple', 'cat', 'fox', 'banana', 'spring', 'hello', 'world']
print(BubbleSort(input))
print(QuickSort(input))
print(insertionSort(input))
print(mergeSort(input))
