import sys
from collections import deque

n, k = map(int, input().split())
array = [] # 디큐 그 자체를 리스트에 넣음 -> 따라서 리스트 안에 deque를 넣었으므로,
array.append(deque(list(map(int, input().split()))))    # 내가 필요한 리스트는 array[0]
print(array)

# 물고기가 가장 많은 어항과 가장 적은 어항의 차이를 구하는 함수
def get_result(array):
    dq = array[0]
    ans = max(dq)- min(dq)
    return ans

# 물고기가 가장 적은 어항에 물고기 한 마리 넣기
def push_fish_to_min_bowl(array):
    array = array[0]
    min_fish = min(array)       # 내부에 deque있으므로
    for i in range(len(array)):
        if array[i] == min_fish:
            array[i] += 1

# 가장 왼쪽의 어항을 위해 쌓기
def popleft_and_stack(array):
    pop = array[0].popleft()    # 가장 왼쪽 어항 위에 쌓자
    array.append(deque([pop]))

# 공중에 뜬 어항들을 시계방향 90도로 회전하기
def rotate_90_clockwise(array):
    new_array = [[0]* len(array) for _ in range(len(array[0]))]
    for i in range(len(array[0])):
        for j in range(len(array)):
            new_array[i][j] = array[j][len(array[0])-1-i]

    print("rotate_90 : ", new_array)

    return new_array

# 2개 이상 쌓인 어항들을 분리해서 공중부양 시키기
def fly_blocks(array):
    while True:
        # 만약 array[0]은 가장 아래 하단의 길이고, array[-1]은 그 위의 층의 개수
        if len(array) > len(array[0]) - len(array[-1]):
            break
        # 뭉쳐지는 블록
        fly_blocks = []
        fly_blocks_row = len(array)
        fly_blocks_col = len(array[-1])

        #  fly_blocks도 단위로 뭉쳐놔...
        for i in range(fly_blocks_row):
            new_deque = deque()
            for _ in range(fly_blocks_col):
                new_deque.append(array[i].popleft())
            fly_blocks.append(new_deque)

        # array -> 마지막 줄 / rotated_block은 위에 쌓이는 블록
        array = [array[0]]  # 맨 아래층의 deque를 다시 정의한다.
        rotated_blocks = rotate_90_clockwise(fly_blocks) # rotated 값만 포함되는 것!!

        # 새로만든 마지막 줄 위로 움직인 블록들을 그 위해 deque 형식으로 올림
        for row in rotated_blocks:
            array.append(deque(row))

        print("함수 끝", array)

    return array

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 공중 부양 작업이 끝난 뒤, 어항의 물고기 수 조절 -> BFS 수행?
def fix_fish_num(array):
    # queue 리스트 집합의 각 리스트에 해당하는 열마다 visited같이 탐색할 초기화 값 넣어줌
    dp = [[0]*len(array[x]) for x in range(len(array))]
    for x in range(len(array)):
        for y in range(len(array[x])):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 주의!!!
                if 0<=nx<len(array) and 0<=ny<len(array[nx]):
                    # 현재 칸이 인접한 칸보다 크다면
                    if array[x][y] > array[nx][ny]:
                        value = (array[x][y]- array[nx][ny])//5
                        # 값이 1보다 작다면, 빼주기
                        if value >= 1:
                            dp[x][y] -= value
                    # 현재의 칸이 인접한 칸보다 작다면
                    else:
                        value = (array[nx][ny] - array[x][y])//5
                        # 값이 1보다 크면 차이 만큼 받는다
                        if value>=1:
                            dp[x][y] += value

    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] += dp[i][j]

    print(array)

#  다시 어항을 일렬로 놓는다.
def put_bowl_in_a_row(array):
    new_array = deque()

    # 어항의 오른쪽부터

    # array[-1]은 맨 위의 값
    for i in range(len(array[-1])):
        for j in range(len(array)):
            new_array.append(array[j][i])

    # 어항의 맨 윗줄부터 마지막 줄까지
    for i in range(len(array[-1]), len(array[0])):
        new_array.append(array[0][i]) # array 그 자체에 리스트가 쓰여있으므로?

    print(new_array)
    result_list = list()
    result_list.append(new_array)

    return result_list

def rotate_180_clockwise(array):
    new_array = []
    # 반대로
    for i in reversed(range(len(array))):
        array[i].reverse()
        new_array.append(array[i])
    print(new_array)
    return new_array

# 다시 공중부양 작업 -> 이번에는 절반을 자르는데, 2번 수행한다.
def fly_blocks_v2(array):
    print("fly_blocks_v2",array)
    left1 = list()
    left2 = list()
    new_deque = deque()
    print(array[0])
    for i in range(n//2):
        new_deque.append(array[0].popleft())

    left1.append(new_deque)
    rotated_left1 = rotate_180_clockwise(left1)
    array += rotated_left1

    for i in range(2):
        tmp_deque = deque()
        for j in range(n//4):
            tmp_deque.append(array[i].popleft())
        left2.append(tmp_deque)

    rotated_left2 = rotate_180_clockwise(left2)
    array += rotated_left2



# 본 함수
cnt =0
while True:
    # 한 섹션 실행하면
    result = get_result(array)
    if result <= k:
        print(result)
        break
    # 받은 케이스에서 가장 작은 수에 +1만큼 해주기
    push_fish_to_min_bowl(array)
    popleft_and_stack(array)    # 가장 왼쪽 값을 행 바꿔주기
    array = fly_blocks(array)   # 공중 부양
    fix_fish_num(array)
    array = put_bowl_in_a_row(array)
    fly_blocks_v2(array)
    fix_fish_num(array)
    array = put_bowl_in_a_row(array)
    result +=1

