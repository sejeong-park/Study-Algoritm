# 백준 문제
| 문제                                                | 제목                | 일자         |기타|
|---------------------------------------------------|-------------------|------------|---|
| [백준 20551](https://www.acmicpc.net/problem/20551) | Sort 마스터 배지훈의 후계자 | 2023.01.18 ||


# 개념

### 순차 탐색

리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

-> 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 주로 사용

주로 사용하는 것

* 리스트에 특정한 값의 원소가 있는지 체크할 때
* 리스트 자료형에서 틍정한 값을 가지는 원소의 개수를 세는 `count()`메서드를 이용할 때

```commandline
# 순차 탐색 코드
def sequential_search(n, target, array) :
    # 각 원소를 하나씩 확인하며
    for i in range(n) :
        if array[i] == target:
        retrun i+1 # 현재의 위치 반환(인덱스는 0부터 시작하므로)

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오")
input_data = input().split()
n = int(input_data[0])
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
```

### 이진 탐색

배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘

한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)

* 절반씩 데이터를 줄어들도록 만든다 (=퀵정렬과 유사)

```commandline
# 재귀함수를 이용하는 방법
def binary_search(array, target, start, end) :
    if start > end :
        return None
    mid = (start + end) // 2
    
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
        
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target : 
        return binary_search(array, target, start, mid-1)
        
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
        
    
    # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
    n, target = list(map(int, input().split())
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))
    
    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n-1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)
```

```commandline
# 반복문으로 구현한 이진 탐색 코드
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
            
    retun None
    
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
```


