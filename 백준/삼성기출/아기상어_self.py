# 16236 - 아기 상어
from collections import deque
n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

#   아기 상어의 현재 위치와 현재 사이즈를 지정해줌
now_size = 2
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x , now_y = i,j

def bfs(x,y):


bfs(now_x, now_y)