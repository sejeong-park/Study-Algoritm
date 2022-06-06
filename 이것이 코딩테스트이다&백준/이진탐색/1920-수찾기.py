n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
m_array = list(map(int, input().split()))


def binary_search(array, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for idx in m_array:
    print(binary_search(array, idx, 0, n-1))