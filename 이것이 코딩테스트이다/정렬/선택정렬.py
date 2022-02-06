"""
선택 정렬
가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고,
그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸는 과정을 반복
"""
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j

    array[i], array[min_idx] = array[min_idx], array[i]

print(array)