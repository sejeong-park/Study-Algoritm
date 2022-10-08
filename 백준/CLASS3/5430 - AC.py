import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    func = input().rstrip()
    n = int(input())
    array = input().rstrip()[1:-1].split(',')
    queue = deque(array)
    rev, flag = 0, 0
    if n == 0:
        queue = []

    for idx in func:
        if idx == 'R':
            rev += 1
        elif idx == 'D':
            if len(queue)!=0:
                # 회전이 두번 되면 원본 : 짝수이면 맨 앞 값이 빠짐
                if rev%2==0:
                    queue.popleft()
                # 회전이 홀수이면 맨 뒤 값이 빠짐
                else:
                    queue.pop()
            else:
                flag = 1
                print('error')
                break

    if flag == 0:
        # 회전이 짝수(원본)이면 reverse 없이 그냥 출력
        if rev%2==0:
            print("["+','.join(queue)+']')
        # 회전이 홀수이면 REVERSE 적용 되므로 변환하여 출력
        else:
            queue.reverse()
            print('['+','.join(queue)+']')



