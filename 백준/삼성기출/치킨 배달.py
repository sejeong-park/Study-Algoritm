# 15686 :: 치킨 배달
from itertools import combinations

n, m = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
total_chicken, total_house = [],[]

for i in range(n):
    for j in range(n):
        if array[i][j] == 1:
            total_house.append((i,j))
        if array[i][j] == 2:
            total_chicken.append((i,j))

chicken_case = list(combinations(total_chicken, m))

def distance(house, chicken):
    house_x, house_y = house
    chicken_x, chicken_y = chicken
    return abs(chicken_x - house_x) + abs(chicken_y - house_y)

def make_result(chicken_case):
    total_distance = 0
    for house in total_house:
        each_distance = 1e9
        # 집을 기준으로 치킨집을 순회하며, 최소 거리를 구함
        for chicken in chicken_case:
            chicken_distance = distance(house, chicken)
            each_distance = min(each_distance, chicken_distance)
            #print(each_distance)

        total_distance += each_distance

    return total_distance

result = 1e9
for case in chicken_case:
    result = min(result, make_result(case))

print(result)







