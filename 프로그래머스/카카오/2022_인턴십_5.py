
from collections import deque
rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operation = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

# def rotate_rc(rc):
#     top, left, bottom, right = 0,0, len(rc)-1, len(rc[0])-1
#     tmp_first = rc[top][left]
#     for tmp in range(top, bottom):
#         rc[tmp][left] = rc[tmp+1][left]
#     for tmp in range(left, right):
#         rc[bottom][tmp] = rc[bottom][tmp+1]
#     for tmp in range(bottom, top,-1):
#         rc[tmp][right] = rc[tmp-1][right]
#     for tmp in range(right, left,-1):
#         rc[top][tmp] = rc[top][tmp-1]
#     rc[top][left+1] = tmp_first
#     return rc

def rotate_rc(rc):
    x1, y1, x2, y2 = 0,0, len(rc), len(rc[0])
    tmp_first = rc[x1][y1]
    min_value = 1e9

    min_value = min(min(rc[x1][y1:y2-1]), min_value)
    rc[x1][y1:y2] = rc[x1][y1:y2-1]

    for i in range(x1,x2):
        min_vlaue = min(rc[i][y1], min_value)
        rc[i-1][y1-1] = rc[i][y1]

    min_value = min(min(rc[x2-1][y1:y2]), min_value)
    rc[x2-1][y1:y2-1] = rc[x2-1][y1:y2]

    for i in range(x2-2, x1-2, -1):
        min_value = min(rc[i][y2-1],min_value)
        rc[i+1][y2-1] = rc[i][y2-1]

    rc[x1][y2-1] = tmp_first
    min_value = min(min_value, temp_first)




# def shiftrow_rc(rc):
#     new_rc = [[0]*len(rc)]*len(rc)
#     for idx in range(len(rc)):
#         if idx+1 == len(rc):
#             new_rc[0] = rc[-1]
#         else:
#             new_rc[idx+1] = rc[idx]
#     # print(new_rc)
#     return new_rc
def shiftrow_rc(rc):
    queue = deque(rc)
    queue.appendleft(rc[-1])
    queue.pop()
    rc = list(queue)
    return rc

def solution(rc, operation):

    for move in operation:
        if move == 'Rotate':
            rc = rotate_rc(rc)
        if move == 'ShiftRow':
            rc = shiftrow_rc(rc)
    return rc

print(solution(rc, operation))