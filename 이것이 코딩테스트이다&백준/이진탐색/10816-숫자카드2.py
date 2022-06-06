import bisect

n = int(input())
n_list = list(map(int, input().split()))

n_list.sort()   # 오름차순 정렬

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    first = bisect.bisect_left(n_list, num)
    second = bisect.bisect_right(n_list, num)
    print(second - first, end = ' ')
