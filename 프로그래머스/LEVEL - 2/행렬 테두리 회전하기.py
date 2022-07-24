# 행렬 테두리 회전하기
import sys
def solution(rows, columns, queries):
    answer = []
    cnt = 0
    array = []
    # 처음 array 보드 그리기
    for idx in range(columns):
       array_list = []
       for jdx in range(rows):
           array_list.append(cnt + 1)
           cnt+=1
       array.append(array_list)

    # 탐색 시작
    answer = []
    for query in queries:
        x1, y1, x2, y2 = query

        for idx in range(x1-1,x2-1):
         array[idx][y1-1] = array[idx+1][y1-1]
        for idx in range(y1-1, y2-1):
         array[x2-1][idx] = array[x2-1][idx+1]


    print(array)
    return answer

print(solution(6,6,[[2,2,5,4]]))