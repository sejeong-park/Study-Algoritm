"""
삽입 정렬
삽입 정렬은 필요할 때만 위치를 바꾸므로 < 데이터가 거의 정렬되었을 때 > 훨씬 효율적이다.
특정한 데이터를 적절한 위치에 들어가기 이전에, 그 앞까지의 데이터는 이미 정렬되어 있다고 가정
"""

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):           # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]:       # 한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        else:
            break

print(array)