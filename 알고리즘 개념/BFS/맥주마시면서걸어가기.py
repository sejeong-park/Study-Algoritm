# 9205 - 맥주 마시면서 걸어가기
from collections import deque

def check(home_x, home_y):
    queue = deque([(home_x, home_y)])
    visited = set()
    while queue:
        x, y = queue.popleft()
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return True
        for i in range(n):
            if i not in visited:
                nx, ny = convenient[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    queue.append([nx,ny])
                    visited.add(i)

    return False

t = int(input())
for _ in range(t):
    n = int(input())
    home_x, home_y = map(int, input().split())
    convenient = []
    for _ in range(n):
        conv_x, conv_y = map(int, input().split())
        convenient.append([conv_x, conv_y])
    festival_x, festival_y = map(int, input().split())
    if check(home_x, home_y):
        print("happy")
    else:
        print("sad")
