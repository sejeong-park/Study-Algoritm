# 행렬 테두리 회전하기

def solution(rows, columns, queries) :
    answer = []
    array = [[0 for col in range(columns)] for row in range(rows)]
    cnt = 1
    for row in range(rows):
        for col in range(columns):
            array[row][col] = cnt
            cnt += 1

    for x1, y1, x2, y2 in queries:
        start_point = array[x1-1][y1-1]
        minimum = start_point

        for idx in range(x1-1, x2-1):
            tmp = array[idx+1][y1-1]
            array[idx][y1-1] = tmp
            minimum = min(minimum, tmp)
        for idx in range(y1-1, y2-1):
            tmp = array[x2-1][idx+1]
            array[x2-1][idx] = tmp
            minimum = min(minimum, tmp)
        for idx in range(x2-1,x1-1, -1):
            tmp = array[idx-1][y2-1]
            array[idx][y2-1] = tmp
            minimum = min(minimum, tmp)
        for idx in range(y2-1, y1-1, -1):
            tmp = array[x1-1][idx-1]
            array[x1-1][idx] = tmp
            minimum = min(minimum, tmp)

        array[x1-1][y1] = start_point
        answer.append(minimum)
    return answer

print(solution(100,97,[[1,1,100,97]]))