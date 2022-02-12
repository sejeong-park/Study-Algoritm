# 징검다리
distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()
    while start<=end:
        mid = (start + end)//2
        del_stone, pre_stone = 0, 0
        for rock in rocks:
            # 바위와 현재 위치 사이의 거리
            if rock - pre_stone < mid:
                del_stone +=1
            else:
                pre_stone = rock
            if del_stone>n:
                break

        if del_stone <= n:
            answer = mid
            start = mid+1
        else:
            end = mid-1
    return answer

print(solution(distance, rocks, n))