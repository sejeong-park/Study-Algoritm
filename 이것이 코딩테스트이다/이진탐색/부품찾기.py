n=int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

answer = []
for idx in m_list:
    result = binary_search(n_list, idx, 0, n-1)
    if result != None:
        answer.append("yes")
    else:
        answer.append("no")

print(" ".join(answer))

