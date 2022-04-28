# 23291 어항정리
from collections import deque
import sys
n = int(input())
student = dict()
for _ in range(n*n):
    array = list(map(int, input().split()))
    student[array[0]] = array[1:]

seat = [[0]*n for _ in range(n)] # 학생의 자리

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 좋아하는 사람 여부 찾기
def find_seat(x,y, key):
    lover_cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n:
            # 좋아하는 사람 찾기
            if seat[nx][ny] in student[key]:
                lover_cnt +=1
    return lover_cnt

def find_empty(dot):
    empty_cnt = 0
    x , y = dot[0], dot[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and seat[nx][ny] == 0:
            empty_cnt+=1

    return empty_cnt

# 학생 마다 찾기
for key, value in student.items():
    lover_cnt_list = dict()
    empty_cnt_list = dict()
    # 학생의 자리 찾기
    for i in range(n):
        for j in range(n):
            if seat[i][j] == 0:
                lover_cnt =  find_seat(i,j, key)

                if lover_cnt  not in lover_cnt_list:
                    lover_cnt_list[lover_cnt] = []
                lover_cnt_list[lover_cnt].append((i,j))

    # 자리 찾기 완료되면, emtpy와 lover의 max값 구하기
    max_lover_cnt = max(lover_cnt_list.keys())
    # 만약 lover이 제일 큰게 하나 있다면, final 값 리턴
    if len(lover_cnt_list[max_lover_cnt]) == 1:
        final_x, final_y = lover_cnt_list[max_lover_cnt][0]
        seat[final_x][final_y] = key

    # 만약 1개가 아닐 경우
    else:
        for idx in lover_cnt_list[max_lover_cnt]:
            empty_cnt = find_empty(idx)
            if empty_cnt not in empty_cnt_list:
                empty_cnt_list[empty_cnt] = []
            empty_cnt_list[empty_cnt].append(idx)

        max_empty_cnt = max(empty_cnt_list.keys())

        if len(empty_cnt_list[max_empty_cnt]) == 1:
            final_x, final_y = empty_cnt_list[max_empty_cnt][0]
        else:
            empty_cnt_list[max_empty_cnt].sort(key = lambda x : x[0])
            final_x, final_y = empty_cnt_list[max_empty_cnt][0]
        seat[final_x][final_y] = key
total_result = 0
### 학생의 만족도 조사
for i in range(n):
    for j in range(n):
        lover_cnt = find_seat(i,j, seat[i][j])
        if lover_cnt == 1:
            total_result += 1
        if lover_cnt == 2:
            total_result += 10
        if lover_cnt == 3:
            total_result += 100
        if lover_cnt == 4:
            total_result += 1000


print(total_result)