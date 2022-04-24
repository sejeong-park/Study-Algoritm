from itertools import combinations
n = int(input())
array = [list(input().split()) for _ in range(n)]
teacher_list, none_list = [], []
tmp_array = array
for i in range(n):
    for j in range(n):
        if array[i][j] == 'T':
            teacher_list.append((i,j))
        if array[i][j] == 'X':
            none_list.append((i,j))

def watch(x,y,direction):
    # 왼쪽 방향 감시
    if 0<=x<n and 0<=y<n:
        if array[x][y] == 'S':
            return True
        if array[x][y] == 'O':
            return False

        if direction == 0:
            watch(x,y-1,0)
        if direction == 1:
            watch(x,y+1,1)
        if direction == 2:
            watch(x-1, y, 2)
        if direction == 3:
            watch(x+1, y,3)


# 장애물 설치 이후에, 한명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for teacher in teacher_list:
        x, y = teacher[0], teacher[1]
        for i in range(4):
            if watch(x,y,i):
                return True # 학생 감지 여부

    return False


find = False # 학생이 한 명도 감지되지 않도록 설치 여부
for case in combinations(none_list, 3):
    # 장애물 설치
    for wall in case:
        array[wall[0]][wall[1]] = 'O'

    # 학생이 한명도 감지되지 않는 경우
    if not process():
        find = True
        break
    array = tmp_array


if find :
    print('YES')
else:
    print('NO')