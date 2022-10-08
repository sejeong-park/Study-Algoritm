# 21609 - 상어 중학교

from collections import deque
import sys

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
print(array)
max_block = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def max_block(x,y, block_num):
    visited = [[False]*n for _ in range(n)]
    queue = deque([(x,y)])
    block_list = [(x,y)]
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if (array[nx][ny] == block_num or array[nx][ny] == 0 ) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
                    block_list.append((nx,ny))
    return block_list



def make_block_group():
    block_dict = dict()
    # 블록이 가장 큰 그룹 찾기 / 같은 번호끼리도!
    for i in range(n):
        for j in range(n):
            if not in
            block_list = max_block(i,j,array[i][j])
            if len(block_list) not in block_dict.keys():
                block_dict[len(block_list)] = []
            else:
                block_dict[len(block_list)].append(block_list)
    max_num = max(block_dict.keys())
    max_list, block_dict = block_dict[max_num], dict()

    print(max_list)

    for idx in max_list:
        print(idx.sort(reverse = True))




make_block_group()




