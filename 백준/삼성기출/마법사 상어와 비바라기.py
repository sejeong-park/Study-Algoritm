# 23288 - 주사위 굴리기 2
from collections import deque

n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]