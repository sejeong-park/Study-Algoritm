#  21610 - 마법사 상어와 비바리기
from collections import deque
import sys

# 서 북서 북 북동 동 남동 하 남서
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

n,m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)]


def make_rain(cloud,d,s):
    x, y = cloud[0], cloud[1]
    nx = (x + dx[d]*s)%n
    ny = (y + dy[d]*s)%n
    if nx<0:
        nx = x - nx
    if ny<0:
        ny = y - ny
    return nx,ny

def copy_magic(new_cloud):
    for cloud in new_cloud:
        x, y = cloud[0], cloud[1]
        water_cnt = 0
        for i in range(4):
            # 홀수 단위만
            nx = x + dx[i*2 + 1]
            ny = y + dy[i*2 + 1]

            if 0<=nx<n and 0<=ny<n and array[nx][ny] !=0:
                water_cnt +=1
        array[x][y] +=water_cnt


    return array

def find_cloud(array, cloud):
    new_cloud = []
    for i in range(n):
        for j in range(n):
            if array[i][j]>=2 and (i,j) not in cloud:
                array[i][j] -=2
                new_cloud.append((i,j))
    return new_cloud


for _ in range(m):
    d, s = map(int,input().split())
    new_cloud = []
    # 구름이 끝난 다음 물 복사 마법을 시작해야함
    for cloud in clouds:
        x, y = make_rain(cloud, d-1, s)
        array[x][y] += 1
        new_cloud.append((x,y))
    array = copy_magic(new_cloud)
    clouds = find_cloud(array, new_cloud)

# 마지막 물의 양 합치기
result = 0
for i in range(n):
    for j in range(n):
        result+=array[i][j]

print(result)









