# 정렬된 배열에서 특정 수의 개수 구하기

n, x = map(int, input().split())
array = list(map(int,input().split()))

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if (mid == 0 or array[mid-1]<target ) and array[mid] == target:
        return mid
    elif array[mid]>= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2

    if (mid == N-1 or array[mid+1]>target) and array[mid]==target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)

N = len(array)
start = 0
end = N-1

first_index = first(array, x, start, end)
if first_index == None:
    print(-1)
else:
    last_index = last(array, x, start, end)
    print(last_index-first_index+1)


