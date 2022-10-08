# 14890 - 경사로

n, l = map(int, input().split())
# 처음 배열 담고, 세로 배열을 가로로 변환 시키기
array = [list(map(int, input().split())) for _ in range(n)]
col_array = []
for i in range(n):
    tmp_list = array[i]
    for j in range(n):
        if i == 0:
            col_array.append([tmp_list[j]])
        else:
            col_array[j].append(tmp_list[j])
array = array + col_array

def solution(road):
    visited = [False for _ in range(n)]

    for i in range(0,n-1):
        # 1. 다음과 현재가 같을 경우 넘어감
        if road[i] == road[i+1]:
            continue
        # 2. 다음이 현재보다 차이가 1 이상 난다면 불가하므로 False
        if abs(road[i]-road[i+1]) > 1:
            return False
        # 3. 현재 블록이 다음블록보다 클 때
        if road[i] > road[i+1]:
            tmp = road[i+1] # 경사로 놓기 가능 여부 탐색
            for k in range(i+1, i+1+l):
                # 그래도 범위 내에 있어야 함
                if 0<= k < n:
                    if road[k] != tmp: # 경사로를 설치 못할 경우
                        return False
                    if visited[k] == True: # 경사로가 이미 있을 경우
                        return False
                    visited[k] = True
                # 범위 밖에 있으면 False
                else:
                    return False
        # 4. 현재 블록이 다음블록보다 작을 때
        if road[i] < road[i+1]:
            tmp = road[i]
            # 반대로 작아지는 경우
            for k in range(i, i-l, -1):
                if 0<= k < n:
                    if road[k] != tmp:
                        return False
                    if visited[k] == True:
                        return False
                    visited[k] = True
                else:
                    return False
    return True

cnt = 0
for tmp_list in array:
    if solution(tmp_list):
        #print(tmp_list)
        cnt+=1

print(cnt)