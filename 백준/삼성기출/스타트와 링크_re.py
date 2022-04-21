from itertools import combinations

n=int(input())
array = [x for x in range(n)]   # member
cases = list(combinations(array, int(n//2)))

print(cases)
for i in range(n):
    array[i] = list(map(int, input().split()))

min_value = 1e9

for case_a in cases:
    stat_a, stat_b = 0,0
    for x in case_a:
        for y in case_a:
            stat_a += array[x][y]
    #print(stat_a)

    case_b = [x for x in range(n) if x not in case_a]
    for x in case_b:
        for y in case_b:
            stat_b += array[x][y]

    min_value = min(min_value, abs(stat_a - stat_b))

print(min_value)