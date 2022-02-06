"""
퀵 정렬
정렬 라이브러리의 근간이 되는 알고리즘

기준 데이터를 설정하고, 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꿈

피벗  : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준

"""

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <=1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [x for x in tail if x<=pivot]   # 분할된 왼쪽 부분
    right_side = [x for x in tail if x>pivot]   # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))