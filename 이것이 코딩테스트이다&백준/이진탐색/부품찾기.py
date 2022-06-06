# 부품 찾기 - 다시 풀기

n = int(input())
n_array = list(map(int, input().split()))
n_array.sort()
m = int(input())
m_array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start + end)//2

    if array[mid] == target:
        return mid

    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for idx in m_array:
    result = binary_search(n_array, idx, 0, n-1)
    #print(result)
    if result != None :
        print('yes', end =' ')
    else:

       print('no', end = ' ')

