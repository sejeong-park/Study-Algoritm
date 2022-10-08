
from collections import deque
rc = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
operation = ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]

def rotate_rc(rc):
    top, left, bottom, right = 0,0, len(rc)-1, len(rc[0])-1
    tmp_first = rc[top][left]
    for tmp in range(top, bottom):
        rc[tmp][left] = rc[tmp+1][left]
    for tmp in range(left, right):
        rc[bottom][tmp] = rc[bottom][tmp+1]
    for tmp in range(bottom, top,-1):
        rc[tmp][right] = rc[tmp-1][right]
    for tmp in range(right, left,-1):
        rc[top][tmp] = rc[top][tmp-1]
    rc[top][left+1] = tmp_first
    return rc


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