# 2457 - 공주님의 정원

n = int(input())

flowers = []

for i in range(n):
    start_mon, start_day, end_mon, end_day = map(int, input().split())
    start = start_mon * 100 + start_day
    end = end_mon * 100 + end_day
    flowers.append([start, end])

# 먼저 피고, 지는 순서 대로 정렬
flowers.sort(key = lambda x:(x[0], x[1]))

cnt = 0
target = 301 # 공주님이 좋아하는 구간
max_date = 0 # 제일 늦게 지는 꽃 비교
for flower_start, flower_end in flowers:
    # 공주님이 좋아하는 구간 (3.1~11.30을 초과하는 경우 반복 종료)
    if target > 1130 or target < flower_start :
        break

    # 꽃의 개수 길이만큼 반복하여 구간별 꽃 비교
    if target >= flower_start :
        # 꽃이 지는 마지막 날이 더 작으면 갱신 -> max 개념
        if max_date <= flower_end :
            max_date = flower_end
    else :
        break

    target = max_date

    cnt +=1

print(cnt)


#     # 꽃을 피울 수 있는 구간
#     if flower_start <= start < flower_end :
#         # 시작 구간의 중복 없이 카운트를 계산하기 위함
#         if check != start :
#             print(flower_start, flower_end)
#             check = start
#             cnt+=1
#
#         # 만약 꽃을 피울 수 있는 구간인데 마지막 date를 초과하는 경우 갱신
#         if max_date < flower_end :
#             max_date = flower_end
#     # 꽃을 피우지 못하는 경우
#     else:
#         # 꽃을 피울 수 있는 경우 저장해두었던 시작값 !
#         # 값 이을때?
#         if check == start :
#             if flower_start <= max_date < flower_end:
#                 print(flower_start, flower_end)
#                 start = max_date # 꽃을 피우지 못한 경우면,
#                 check = start
#                 max_date = flower_end
#                 cnt += 1
#         else :
#             if start<flower_start :
#                 cnt = 0
#                 break
#
# if max_date <= 1130:
#     cnt = 0
#
# print(cnt)
#
#
