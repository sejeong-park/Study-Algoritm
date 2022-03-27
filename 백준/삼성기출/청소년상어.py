#-*- coding: utf-8 -*-

import copy
# 4*4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None]*4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        array[i][j] = [data[j*2], data[j*2+1]-1]

# 8가지 방향에 대한 정의 (차례대로!)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1)%8

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 ( 낮은 번호부터 ) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None:
            x,y = position[0], position[1]
            direction = array[x][y][1]

            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            