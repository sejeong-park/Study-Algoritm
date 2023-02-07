import heapq
def quick_sort(x):
	if len(x) < 2:
		return x

	pivot = x[len(x) // 2]
	left_side, right_side, equal = [], [], []

	for i in x:
		if i < pivot :
			left_side.append(i)
		elif i > pivot :
			right_side.append(i)
		else:
			equal.append(i)

	return quick_sort(left_side) + equal + quick_sort(right_side)

def quick_sort_2(x):
	if len(x) < 2:
		return x

	pivot, tail = x[0], x[1:]

	left_side = [a for a in tail if a <= pivot]
	right_side = [a for a in tail if a > pivot]

	return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

input = [3,7,2,1,6,8,10, 6, 53, 1]

print(quick_sort(input))
print(quick_sort_2(input))